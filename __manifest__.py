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
        'views/property_tag_views.xml',
        'views/property_offer_views.xml',
    ],
    'installable': True,
    'application': True,
}
