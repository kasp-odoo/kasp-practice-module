# -*- coding: utf-8 -*-
from odoo import fields,models

class BloodConnectDonationCenter(models.Model):
    _name = "blood.connect.donation.center"
    _description = "Blood Connect Donation Center Model"

    name = fields.Char(string='Center Name', required=True)
    address = fields.Text(required=True)
    contact = fields.Char(string='Contact Number', required=True)
    capacity = fields.Integer(string='Capacity', required=True)
    blood_group = fields.Many2one('blood.connect.blood.type', string='Blood Group')
   
# Email: Char Field, to store the email of the center
# Donation Requests: One2many Field, to connect with Blood Donation Request model and store the requests for blood donation
# Blood Transactions: One2many Field, to connect with Blood Transaction model and store the transactions of blood donation and delivery.