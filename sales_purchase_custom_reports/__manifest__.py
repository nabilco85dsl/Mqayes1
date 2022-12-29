# -*- coding: utf-8 -*-
{
    'name': "sales_purchase_custom_reports",
    'author': "Mohamed Slah",
    'category': 'Sales,Purchase',
    'version': '15.0',
    'depends': ['base','sale','sale_management','purchase','l10n_sa_invoice'],
    'data': [
        'views/res_company.xml',
        'reports/purchase_report.xml',
        'reports/sales_report.xml',
        'reports/account_move_report.xml',
    ],

}
