# -*- coding: utf-8 -*-
{
    'name': 'Paraguay - Accounting',
    'website': "https://www.avatar.com.py",
    'icon': '/account/static/description/l10n.png',
    'countries': ['py'],
    'version': '0.2',
    'description': """
""",
    'author': "Avatar Informaticca S.R.L.",
    'category': 'Accounting/Localizations/Account Charts',
    'depends': [
        'l10n_latam_invoice_document',
        'l10n_latam_base',
        'account_tax_python',
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/l10n_latam_identification_type_data.xml',
        'data/l10n_py_set_responsibility_type_data.xml',
        #'data/account_chart_template_data2.xml',
        'data/uom_uom_data.xml',
        #'data/l10n_latam.document.type.csv',
        'data/l10n_latam_document_type_data.xml',
        'data/res_partner_data.xml',
        'data/res_currency_data.xml',
        'data/res.country.csv',
        'data/res_country_state_data.xml',
        'data/l10n_py_district_data.xml',
        'data/l10n_py_city_01.xml',
        'data/l10n_py_city_02.xml',
        'data/l10n_py_city_03.xml',
        'data/l10n_py_city_04.xml',
        'data/l10n_py_city_05.xml',
        'data/l10n_py_city_06.xml',
        'data/l10n_py_city_07.xml',
        'data/l10n_py_city_08.xml',
        'data/l10n_py_city_09.xml',
        'data/l10n_py_city_10.xml',
        'data/l10n_py_city_11.xml',
        'data/l10n_py_city_12.xml',
        'data/l10n_py_city_13.xml',
        'data/l10n_py_city_14.xml',
        'data/l10n_py_city_15.xml',
        'data/l10n_py_city_16.xml',
        'data/l10n_py_city_17.xml',
        'data/l10n_py_city_18.xml',
        'data/l10n_py_city_19.xml',
        'data/l10n_py_city_20.xml',

        #'views/account_move_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'views/res_country_view.xml',
        #'views/afip_menuitem.xml',
        #'views/l10n_ar_afip_responsibility_type_view.xml',
        #'views/res_currency_view.xml',
        #'views/account_fiscal_position_view.xml',
        'views/uom_uom_view.xml',
        'views/account_journal_view.xml',
        #'views/l10n_latam_document_type_view.xml',
        #'views/report_invoice.xml',
        #'views/res_config_settings_view.xml',
        #'report/invoice_report_view.xml',
    ],
    'demo': [
        #'demo/exento_demo.xml',
        #'demo/mono_demo.xml',
        'demo/respinsc_demo.xml',
        #'demo/res_partner_demo.xml',
        #'demo/product_product_demo.xml',
        #'demo/account_customer_invoice_demo.xml',
        #'demo/account_customer_refund_demo.xml',
        #'demo/account_supplier_invoice_demo.xml',
        #'demo/account_supplier_refund_demo.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
    'pre_init_hook': '_set_change_values',
}
