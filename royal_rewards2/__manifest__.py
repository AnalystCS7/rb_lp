# -*- coding: utf-8 -*-
{
    'name': 'Royal Rewards v2',
    'summary': 'Loyalty program for RoyalBeards',
    'description': 'A loyalty program for the RoyalBeards ecommerce platform',
    'author': 'RoyalBeards Lda.',
    'category': 'Sales/Loyalty',
    'version': '1.0',
    'depends': ['base', 'sale', 'website'],
    'data': [
        'security/reward_security.xml',
        'data/reward_point_data.xml',
        'data/reward_point_rule_data.xml',
        'data/reward_point_tier_data.xml',
        'data/ir_cron_data.xml',
        'views/reward_point_views.xml',
        'views/reward_point_rule_views.xml',
        'views/reward_point_tier_views.xml',
        'views/main_views.xml',
    ],
    'qweb': [
        'static/src/xml/reward_point.xml',
    ],
    'application': True,
    'installable': True,
}
