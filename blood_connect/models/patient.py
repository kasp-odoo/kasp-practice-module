# -*- coding: utf-8 -*-
from odoo import fields, models


class Patient(models.Model):
    _name = "patient.patient"
    _description = "Blood Connect Patient Model"

    name = fields.Char(string='Patient Name', required=True)
    phone = fields.Char(string='Phone Number', required=True)
    address = fields.Char(string='Address', required=True)
    age = fields.Integer(required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', required=True)
    blood_group = fields.Many2one('blood.type', string='Blood Group')
    # patient ID
    health_info = fields.Text(
        string='Health Information (Reason)', required=True)
