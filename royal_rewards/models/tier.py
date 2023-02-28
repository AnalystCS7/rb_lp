from odoo import models, fields, api, _

class Tier(models.Model):
    _name = 'royalrewards.tier'
    _description = 'Tier for Royal Rewards'

    name = fields.Char(string='Name')
    min_points = fields.Integer(string='Minimum Points')
    max_points = fields.Integer(string='Maximum Points')
    point_conversion = fields.Float(string='Point Conversion')
    description = fields.Text(string='Description')

    @api.constrains('min_points', 'max_points')
    def _check_tier_points(self):
        for record in self:
            if record.min_points > record.max_points:
                raise ValidationError(_('The minimum points must be less than the maximum points.'))
