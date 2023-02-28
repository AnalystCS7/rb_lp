from odoo import models, fields


class Reward(models.Model):
    _name = "royalbeards.reward"
    _description = "Royal Rewards"

    name = fields.Char(required=True)
    description = fields.Char()
    points = fields.Integer(required=True, default=0)
    reward_type = fields.Selection(
        [("amount_off", "Amount Off"), ("%_off", "% Off"), ("specific_item", "Specific Item")],
        required=True,
        default="amount_off",
    )
    discount_value = fields.Float(
        string="Discount Value",
        help="The value of the discount (as amount or percentage depending on the type of reward)",
    )
    apply_to = fields.Selection(
        [("next_order", "Next Order"), ("specific_item", "Specific Item")],
        required=True,
        default="next_order",
    )
    valid_days = fields.Integer(string="Validity (days)")
    active = fields.Boolean(default=True)
