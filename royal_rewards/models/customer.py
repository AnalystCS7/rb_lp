from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    reward_points = fields.Float(string='Reward Points', default=0.0)
    reward_tier_id = fields.Many2one('res.partner.reward.tier', string='Reward Tier', compute='_compute_reward_tier', store=True)

    @api.depends('reward_points')
    def _compute_reward_tier(self):
        tiers = self.env['res.partner.reward.tier'].search([], order='min_points desc')
        for partner in self:
            for tier in tiers:
                if partner.reward_points >= tier.min_points:
                    partner.reward_tier_id = tier
                    break
