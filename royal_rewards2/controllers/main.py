# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class RoyalRewards(http.Controller):
    @http.route('/royal_rewards/info', type='http', auth='public', website=True)
    def rewards_info(self, **kw):
        reward_rules = request.env['reward.point.rule'].sudo().search([])
        reward_tiers = request.env['reward.point.tier'].sudo().search([])
        return request.render('royal_rewards.rewards_info', {
            'reward_rules': reward_rules,
            'reward_tiers': reward_tiers,
        })
