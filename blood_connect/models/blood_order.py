# -*- coding: utf-8 -*-
from odoo import fields, models


class BloodOrder(models.Model):
    _name = "blood.order"
    _description = "Blood Connect Order Model"

    # order_id = fields.Char(string='Order ID', required=True)
    order_date = fields.Date(string='Order Date', required=True, readonly=True)
    blood_unit = fields.Integer(string='Blood Unit(s)', required=True)
    blood_group = fields.Many2one('blood.type', string='Blood Group')
    name = fields.Char(string='Patient/Hospital Name', required=True)
    delivery_date = fields.Date(string='Delivery Date', required=True)
    delivery_loc = fields.Char(string='Delivery Location', required=True)
    state = fields.Selection(
        selection=[('confirmed', 'Confirmed'),
                   ('delivered', 'Delivered'),
                   ('cancelled', 'Cancelled')], string='State', copy=False)
    # Order Approver (Blood Bank or Donation Center Representative)
