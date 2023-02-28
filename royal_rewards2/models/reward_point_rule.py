from odoo import fields, models

class RewardPointRule(models.Model):
    _name = 'reward.point.rule'
    _description = 'Reward Point Rule'

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Start Date', default=fields.Date.today())
    end_date = fields.Date(string='End Date', required=True)
    validity = fields.Selection(selection=[('lifetime', 'Lifetime'), ('period', 'Period')], string='Validity', required=True)
    min_amount = fields.Float(string='Minimum Amount', default=0.0, required=True)
    points_multiplier = fields.Float(string='Points Multiplier', default=1.0, required=True)
    tier_id = fields.Many2one(comodel_name='reward.point.tier', string='Tier')
