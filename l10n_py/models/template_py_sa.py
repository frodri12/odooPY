# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, _
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('py_sa')
    def _get_py_sa_template_data(self):
        return {
            'name': _('Paraguay Generic Chart of Accounts for Registered Accountants'),
            'parent': 'py_ex',
            'code_digits': '12',
        }

    @template('py_sa', 'res.company')
    def _get_py_sa_res_company(self):
        #return {
        #    self.env.company.id: {
        #        'account_fiscal_country_id': 'base.py',
        #        'bank_account_code_prefix': '1.1.1.02.',
        #        'cash_account_code_prefix': '1.1.1.01.',
        #        'transfer_account_code_prefix': '6.0.00.00.',
        #        'account_default_pos_receivable_account_id': 'base_deudores_por_ventas_pos',
        #        'income_currency_exchange_account_id': 'base_diferencias_de_cambio',
        #        'expense_currency_exchange_account_id': 'base_diferencias_de_cambio',
        #        'account_sale_tax_id': 'ri_tax_vat_21_ventas',
        #        'account_purchase_tax_id': 'ri_tax_vat_21_compras',
        #    },
        #}
        return {
            self.env.company.id: {
               'account_fiscal_country_id': 'base.py',
                'bank_account_code_prefix': '1.1.01.12.',
                'cash_account_code_prefix': '1.1.01.04.',
                'transfer_account_code_prefix': '6.1.01.01.',
                'account_default_pos_receivable_account_id': 'py_acc_11020102',
                'income_currency_exchange_account_id': 'py_acc_41010205',
                'expense_currency_exchange_account_id': 'py_acc_41010205',
                'account_sale_tax_id': 'ri_tax_vat_py_10_ventas',
                'account_purchase_tax_id': 'ri_tax_vat_py_10_compras',
            },
        }
