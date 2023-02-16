# -*- coding: utf-8 -*-
from odoo import fields, models


class Donor(models.Model):
    _name = "donor.donor"
    _description = "Blood Connect Donor Model"

    name = fields.Char(string='Donor Name', required=True)
    phone = fields.Char(string='Phone Number', required=True)
    address = fields.Char(string='Address', required=True)
    age = fields.Integer(required=True, default=18)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')], string='Gender', required=True)
    blood_group = fields.Many2one('blood.type', string='Blood Group')
    health_info = fields.Text(string='Health Information')
