# -*- coding: utf-8 -*-
{
    'name': "booking_order_BARON_BETAZARA_17012025",

    'summary': """
        Test For HashMicro""",

    'description': """
        Test For HashMicro
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale','sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/sale_order_views.xml',
        'views/service_team_views.xml',
        'views/work_order_views.xml',
        'wizard/work_order_cancel_views.xml',
        'reports/work_order_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}