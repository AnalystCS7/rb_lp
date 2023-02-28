from odoo import fields, models

class RewardPointTier(models.Model):
    _name = 'reward.point.tier'
    _description = 'Reward Point Tier'

    name = fields.Char(string='Name')
    min_points = fields.Float(string='Minimum Points', required=True)
    max_points = fields.Float(string='Maximum Points', required=True)
    discount_percentage = fields.Float(string='Discount Percentage')
    rule_ids = fields.One2many(comodel_name='reward.point.rule', inverse_name='tier_id', string='Reward Point Rules')
