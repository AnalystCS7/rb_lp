# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class RewardsController(http.Controller):

    @http.route('/royal_rewards/rewards', type='http', auth="user", website=True)
    def rewards(self, **post):
        partner = request.env.user.partner_id
        rewards = partner.rewards
        return request.render('royal_rewards.rewards', {'rewards': rewards})

    @http.route('/royal_rewards/redeem', type='http', auth="user", website=True)
    def redeem(self, **post):
        partner = request.env.user.partner_id
        rewards = partner.rewards
        return request.render('royal_rewards.redeem', {'rewards': rewards})

    @http.route('/royal_rewards/apply_reward', type='http', auth="user", website=True)
    def apply_reward(self, **post):
        order_id = int(post.get('order_id'))
        reward_id = int(post.get('reward_id'))
        order = request.env['sale.order'].browse(order_id)
        reward = request.env['royal.reward'].browse(reward_id)
        order.apply_reward(reward)
        return request.redirect('/shop/checkout')
