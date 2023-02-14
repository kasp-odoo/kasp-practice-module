# -*- coding: utf-8 -*-
from odoo import fields, models


class BloodType(models.Model):
    _name = "blood.type"
    _description = "Blood Connect Blood Type Model"
    _rec_name = "blood_type"

    blood_type = fields.Selection(
        selection = [
            ('A+', 'A+'),
            ('O+', 'O+'),
            ('B+', 'B+'),
            ('AB+', 'AB+'),
            ('A-', 'A-'),
            ('O-', 'O-'),
            ('B-', 'B-'),
            ('AB-', 'AB-'),
        ], string='Blood Type', required=True)
    # Code of blood group
    description = fields.Text(string='Description')
    donate_blood_to = fields.Char(string='Donate Blood To') # required=True
    receive_blood_from = fields.Char(
        string='Receive Blood From') # required=True
