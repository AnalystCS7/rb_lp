# -*- coding: utf-8 -*-
from odoo import http

class royal_rewards_v8(http.Controller):
    @http.route('/royal_rewards_v8/royal_rewards_v8/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/royal_rewards_v8/royal_rewards_v8/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('royal_rewards_v8.listing', {
            'root': '/royal_rewards_v8/royal_rewards_v8',
            'objects': http.request.env['royal_rewards_v8.royal_rewards_v8'].search([]),
        })

    @http.route('/royal_rewards_v8/royal_rewards_v8/objects/<model("royal_rewards_v8.royal_rewards_v8"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('royal_rewards_v8.object', {
            'object': obj
        })