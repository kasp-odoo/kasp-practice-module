# -*- coding: utf-8 -*-
from odoo import fields, models


class DonationCenter(models.Model):
    _name = "donation.center"
    _description = "Blood Connect Donation Center Model"

    name = fields.Char(string='Center Name', required=True)
    address = fields.Char(required=True)
    city = fields.Char(required=True)
    state = fields.Many2one('res.country.state',required=True)
    zip_code = fields.Char(string='Zip Code', required=True)
    contact = fields.Char(string='Contact Number', required=True)
    email = fields.Char()
    capacity = fields.Integer(string='Capacity(Units)', required=True)
    available_blood = fields.Integer(string='Available Units', readonly=True)
    # blood_group = fields.Many2one('blood.type', string='Blood Group')
    order_ids = fields.One2many('blood.request','order_id')
    donation_ids = fields.One2many('donation.request','center_id')