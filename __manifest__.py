{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/real_estate_views.xml',
        'views/real_estate_menus.xml',
        'views/real_estate_search.xml',
        'views/property_type_views.xml',
        'views/property_type_search.xml',
    ],
    'installable': True,
    'application': True,
}
