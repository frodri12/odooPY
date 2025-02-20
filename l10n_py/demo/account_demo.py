# -*- coding: utf-8 -*-
import logging

from odoo import api, models

        #super()._get_demo_data(company) return {
        #    **self._get_demo_data_products(company),
        #    'account.move': self._get_demo_data_move(company),
        #    'account.bank.statement': self._get_demo_data_statement(company),
        #    'account.bank.statement.line': self._get_demo_data_transactions(company),
        #    'account.reconcile.model': self._get_demo_data_reconcile_model(company),
        #    'ir.attachment': self._get_demo_data_attachment(company),
        #    'mail.message': self._get_demo_data_mail_message(company),
        #    'mail.activity': self._get_demo_data_mail_activity(company),
        #    'res.partner.bank': self._get_demo_data_bank(company),
        #    'account.journal': self._get_demo_data_journal(company),
        #}

class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    @api.model
    def _get_demo_data(self, company):    # company=False
        demo_data = super()._get_demo_data(company)
        if company in (
            self.env.ref('base.company_mono', raise_if_not_found=False),
            self.env.ref('base.company_exento', raise_if_not_found=False),
            self.env.ref('base.company_ri', raise_if_not_found=False),
        ):
            # Do not load generic demo data on these companies
            return {}

        if company.account_fiscal_country_id.code == "PY":
            demo_data = {
                'res.partner': demo_data.pop('res.partner', {}),
                **demo_data,
            }
            demo_data['res.partner'].setdefault('base.res_partner_2', {})
            demo_data['res.partner']['base.res_partner_2']['l10n_py_set_responsibility_type_id'] = 'l10n_py.res_CONTPJ'
            demo_data['res.partner'].setdefault('base.res_partner_12', {})
            demo_data['res.partner']['base.res_partner_12']['l10n_py_set_responsibility_type_id'] = 'l10n_py.res_CONTPJ'
        return demo_data

    @api.model
    def _get_demo_data_move(self, company):            # company=False
        data = super()._get_demo_data_move(company)
        if company.account_fiscal_country_id.code == "PY":
            data['demo_invoice_5']['l10n_latam_document_number'] = '1-1'
            data['demo_invoice_equipment_purchase']['l10n_latam_document_number'] = '1-2'
            data['demo_move_auto_reconcile_3']['l10n_latam_document_number'] = '1-3'
            data['demo_move_auto_reconcile_4']['l10n_latam_document_number'] = '1-4'
        return data

    def _post_load_demo_data(self, company=False):
        if company not in (
            self.env.ref('base.company_mono', raise_if_not_found=False),
            self.env.ref('base.company_exento', raise_if_not_found=False),
            self.env.ref('base.company_ri', raise_if_not_found=False),
        ):
            # Do not load generic demo data on these companies
            return super()._post_load_demo_data(company)
