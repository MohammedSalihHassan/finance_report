{   
 'name': 'finance_report',
 'summary': """This module print finance reports""",
 'version': '14.0.1.0.0',
 'description': """This module will add finance reports""",
 'author': 'ALIAICT',
 'company': 'ALIA',
 'website': 'https://www.aliaict.com',
 'category': '',  
 'depends': ['base','account','purchase'],
 'license': 'AGPL-3',
 'data': [
        'security/ir.model.access.csv',
        'views/custom_company_view.xml',
        'views/custom_purchase_order_info_view.xml',
        'report/report_view.xml',
        'report/template/header_footer_template.xml',
        'report/template/journal_entries_template.xml',
        'report/template/account_move_line_template.xml',
        'wizard/finance_tax_wizard_view.xml',
        'wizard/general_ledger_wiz_view.xml',
        'report/template/general_ledger_report_template.xml',
        'report/template/tax_invoice_report_templet.xml',
        'report/template/custom_purchase_order_report_template.xml'

    ],
 'demo': [],
 'installable': True,
 'auto_install': False,
 'application': True,
}