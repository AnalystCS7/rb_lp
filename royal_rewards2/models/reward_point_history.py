from odoo import api, fields, models

class RewardPointHistory(models.Model):
    _name = 'reward.point.history'
    _description = 'Reward Point History'

    name = fields.Char(string='Name', required=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('reward.point.history'))
    reward_point_id = fields.Many2one(comodel_name='reward.point', string='Reward Point')
    points = fields.Float(string='Points', default=0.0)
    description = fields.Char(string='Description')
    date = fields.Datetime(string='Date', default=fields.Datetime.now, readonly=True)
    source = fields.Selection(selection=[('order', 'Order'), ('manual', 'Manual')], string='Source', default='order')

    @api.model
    def create(self, vals):
        res = super(RewardPointHistory, self).create(vals)
        if res.reward_point_id:
            res.reward_point_id.point_balance += res.points
        return res

    def write(self, vals):
        res = super(RewardPointHistory, self).write(vals)
        if self.reward_point_id:
            self.reward_point_id.point_balance = sum(self.reward_point_id.point_history.mapped('points'))
        return res

    def unlink(self):
        res = super(RewardPointHistory, self).unlink()
        for record in self:
            if record.reward_point_id:
                record.reward_point_id.point_balance = sum(record.reward_point_id.point_history.mapped('points'))
        return res
