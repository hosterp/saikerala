{
    'name': 'Hiworth Committee1',
    'version': '1.0',
    'category': 'Committee',
    'sequence': 21,
    'description': """ Committee Management """,
    'depends': ['hr',],
    'data': [
            'views/requirement_new.xml',
            'views/dashboard_view.xml',
            'views/place.xml',
            'views/menu_odoo_remove.xml',
            'views/hr_employee_view.xml',
            'views/res_partner_view.xml',
    ],

    # 'qweb': [
    #     'static/src/xml/popup_notifications.xml',
    # ],

    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}