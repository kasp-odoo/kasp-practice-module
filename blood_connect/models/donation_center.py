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
    capacity = fields.Integer(string='Capacity', required=True)
    blood_group = fields.Many2one('blood.type', string='Blood Group')

# Donation Requests: One2many Field, to connect with Blood Donation Request model and store the requests for blood donation
# Blood Transactions: One2many Field, to connect with Blood Transaction model and store the transactions of blood donation and delivery.

# Add Blood Stock Page (Blood Type -> Blood Units available) use compute
