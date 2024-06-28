{
    'name': 'Inventario_prueba',
    'version': '1.0',
    'summary': 'Modulo para el movimiento de productos',
    'description': 'Modulo para el movimiento de productos en un inventario',
    'author': 'Andres Morantes',
    'category': 'Inventory',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/stock_in_views.xml',
        'views/stock_out_views.xml',
        'views/inventory_menu.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'test': [
            'tests/test_inventory.py',
        ],
}
