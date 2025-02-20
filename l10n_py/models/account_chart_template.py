# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, _
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @api.model
    def _get_py_responsibility_match(self, chart_template):
        """ return responsibility type that match with the given chart_template code
        """
        match = {
            'py_base': self.env.ref('l10n_py.res_CONTPF'),
            'py_ex': self.env.ref('l10n_py.res_CONTPJ'),
            'py_sa': self.env.ref('l10n_py.res_CONTPJ'),
        }
        return match.get(chart_template)

    def _load(self, template_code, company, install_demo):
        """ Set companies SET Responsibility and Country if AR CoA is installed, also set tax calculation rounding
        method required in order to properly validate match AFIP invoices.

        Also, raise a warning if the user is trying to install a CoA that does not match with the defined AFIP
        Responsibility defined in the company
        """
        coa_responsibility = self._get_py_responsibility_match(template_code)
        if coa_responsibility:
            company.write({
                'l10n_py_set_responsibility_type_id': coa_responsibility.id,
                'country_id': self.env['res.country'].search([('code', '=', 'PY')]).id,
                'tax_calculation_rounding_method': 'round_globally',
            })
            # set CUIT identification type (which is the argentinean vat) in the created company partner instead of
            # the default VAT type.
            company.partner_id.l10n_latam_identification_type_id = self.env.ref('l10n_py.it_ruc')

        res = super()._load(template_code, company, install_demo)

        # If Responsable Monotributista remove the default purchase tax
        if template_code in ('py_base', 'py_ex'):
            company.account_purchase_tax_id = self.env['account.tax']

        return res

    def try_loading(self, template_code, company, install_demo=False):
        # During company creation load template code corresponding to the AFIP Responsibility
        if not company:
            return
        if isinstance(company, int):
            company = self.env['res.company'].browse([company])
        if company.country_code == 'AR' and not company.chart_template:
            match = {
                self.env.ref('l10n_py.res_CONTPF'): 'py_base',
                self.env.ref('l10n_py.res_CONTPJ'): 'py_ex',
                self.env.ref('l10n_py.res_CONTPJ'): 'py_sa',
            }
            template_code = match.get(company.l10n_py_set_responsibility_type_id, template_code)
        return super().try_loading(template_code, company, install_demo)
