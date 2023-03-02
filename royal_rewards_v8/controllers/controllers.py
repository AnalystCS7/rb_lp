# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class royal_rewards_v8(http.Controller):
    @http.route('/royal_rewards_v8/royal_rewards_v8/', auth='public', website=True)
    def index(self, **kw):
        User = request.env['res.users']
        users = User.search([])
        user_list = []

        for user in users:
            user_info = {
                'name': user.name,
                'email': user.email,
                'phone': user.phone,
                'country': user.country_id.name,
                'city': user.city,
            }
            user_list.append(user_info)

        return request.render('royal_rewards_v8.user_list', {'user_list': user_list})
