from odoo import api, fields, models

class RewardPoint(models.Model):
    _name = 'reward.point'
    _description = 'Reward Point'

    name = fields.Char(string='Name')
    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    point_balance = fields.Float(string='Point Balance', default=0.0, readonly=True)
    point_history = fields.One2many(comodel_name='reward.point.history', inverse_name='reward_point_id', string='Point History')
    tier_id = fields.Many2one(comodel_name='reward.point.tier', string='Tier')
    state = fields.Selection(selection=[('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active', readonly=True)

    @api.depends('tier_id')
    def _compute_points(self):
        for point in self:
            point.point_balance = 0.0
            if point.tier_id:
                rules = point.tier_id.rule_ids.filtered(lambda r: r.validity and r.validity == 'lifetime' or r.end_date >= fields.Date.today())
                for rule in rules:
                    point.point_balance += rule.compute_points(point.customer_id.total_paid, point.customer_id.reward_points, point.tier_id.id)
            point.point_balance = round(point.point_balance, 2)
