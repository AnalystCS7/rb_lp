from odoo import api, fields, models


class Referral(models.Model):
    _name = 'royalbeards.referral'
    _description = 'Referral'

    name = fields.Char(required=True)
    user_id = fields.Many2one(
        'res.users', string='User', required=True, default=lambda self: self.env.user)
    referred_user_id = fields.Many2one('res.users', string='Referred User', required=True)
    date = fields.Datetime(default=fields.Datetime.now)

    _sql_constraints = [
        ('user_referral_unique', 'unique(user_id, referred_user_id)', 'User can refer a specific user only once.'),
        ('referral_user_unique', 'unique(user_id, name)', 'User can create a referral with same name only once.'),
    ]

    @api.model
    def create(self, vals):
        referral = super(Referral, self).create(vals)
        reward = self.env['royalbeards.reward'].create({
            'customer_id': referral.user_id.partner_id.id,
            'referral_id': referral.id,
            'type': 'signup',
            'points': self.env['ir.config_parameter'].sudo().get_param('royal_rewards.signup_points'),
        })
        reward._onchange_points()
        return referral
