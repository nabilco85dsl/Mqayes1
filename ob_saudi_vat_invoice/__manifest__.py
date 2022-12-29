{
    'name': 'Electronic invoice KSA',
    'version': '14.1.1.5',

    'category': 'Accounting',
    'summary': '',
    
    'description': """
     Electronic invoice KSA
     """,
    "author" : "Ahmed Elomrany",
    "email": 'ah1733@fayoum.edu.eg',
    "license": 'OPL-1',
    'depends': ['account'],
    # 'depends': ['account','l10n_sa_invoice'],

    'data': [
        'report/vat_invoice_report_print.xml',
        'report/vat_report_action_call.xml',
        'report/simpli_vat_invoice_report.xml',
        'views/sale_purchase_invoice_view.xml',
        'report/invoice_default_attach.xml',
    ],
    "price": 20,
    'currency': 'EUR',
    "live_test_url" : "https://youtu.be/K9XG-_2Tw_Q", 
    # Old Live Link
    #"live_test_url" : "https://youtu.be/yS1ReLJcIbk",  
    
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}





