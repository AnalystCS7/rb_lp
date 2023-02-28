# -*- coding: utf-8 -*-
{
    'name': 'Royal Rewards',
    'version': '16.0',
    'category': 'Uncategorized',
    'summary': 'A brief description of my module',
    'description': 'A longer description of my module',
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'views/customer_views.xml',
        'views/reward_views.xml',
        'views/tier_views.xml',
        'views/transaction_views.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
