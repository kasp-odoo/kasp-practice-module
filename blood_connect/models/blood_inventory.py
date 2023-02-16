# -*- coding: utf-8 -*-
from odoo import fields, models


class BloodInventory(models.Model):
    _name = "blood.inventory"
    _description = "Blood Connect Blood Inventory Model"

    quantity = fields.Integer(required=True)
    blood_group = fields.Many2one('blood.type', string='Blood Group')
    expiration_date = fields.Date(string='Expiry Date',readonly=True)
    donation_date = fields.Date(string='Donation Date')
    donation_center = fields.Many2one('donation.center', string='Donation Center')
    status = fields.Selection(
        selection = [
            ('available','Available'),
            ('reserved','Reserved'),
            ('unavailable','Unavailable')])

# Blood type (Many2one field linking to your Blood Type model)
# Quantity (Float field to track the number of units available)
# Expiration date (Date field to track the date on which the blood will expire)
# Donation date (Date field to track when the blood was donated)
# Donation center (Many2one field linking to your Blood Donation Center model to track the origin of the donation)
# Status (Selection field to indicate whether the blood is available, reserved, or unavailable)