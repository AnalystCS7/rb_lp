from odoo import models, fields

class RewardPointType(models.Model):
    _name = 'reward.point.type'
    _description = 'Reward Point Type'

    name = fields.Char(string='Name', required=True, translate=True)
    code = fields.Char(string='Code', required=True)
