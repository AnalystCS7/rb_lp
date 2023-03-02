# -*- coding: utf-8 -*-

from odoo import models, fields, api

class royal_rewards_v8(models.Model):
    _name = 'royal_rewards_v8.model'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    user_id = fields.Many2one('res.users', string='User', required=True)
    
    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100