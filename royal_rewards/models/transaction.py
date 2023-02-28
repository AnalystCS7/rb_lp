from odoo import models, fields, api, _

class Transaction(models.Model):
    _name = 'royalrewards.transaction'
    _description = 'Transaction for Royal Rewards'

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    points = fields.Float(string='Points', required=True)
    transaction_type = fields.Selection([
        ('earn', 'Earn'),
        ('redeem', 'Redeem'),
    ], string='Transaction Type', required=True)
    transaction_date = fields.Date(string='Transaction Date', default=fields.Date.today(), required=True)
    order_id = fields.Many2one('sale.order', string='Order')
