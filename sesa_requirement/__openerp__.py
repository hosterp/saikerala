{
    'name': 'Hiworth Committee1',
    'version': '1.0',
    'category': 'Committee',
    'sequence': 21,
    'description': """ Committee Management """,
    'depends': ['hr','asn_baby_blue','report_xlsx',],
    'data': [
            'views/requirement_new.xml',
            'views/dashboard_view.xml',
            'views/place.xml',
            'views/menu_odoo_remove.xml',
            'views/hr_employee_view.xml',
            'views/res_partner_view.xml',
            'views/template.xml',
            'views/report.xml',
            'views/samithi_details_report.xml',
            'views/revived_samithi.xml',
    ],
    # 'css': [
    #     "static/src/css/styles.css",
    #     ],
    'js': [
        'static/src/js/custom_webclient.js',
    ],
    # 'css': [
    #     'static/src/css/styles.css',
    # ],
    'qweb': [
        "static/src/xml/*.xml",
        # "static/src/css/styles.css",
            # 'static/src/css/template.xml'
        # 'static/src/xml/popup_notifications.xml',
    ],

    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}