# -*- coding: utf-8 -*-
from odoo import fields, models


class Donor(models.Model):
    _name = "donor.donor"
    _description = "Blood Connect Donor Model"

    name = fields.Char(string='Donor Name', required=True)
    phone = fields.Char(string='Phone Number', required=True)
    address = fields.Char(string='Address', required=True)
    city = fields.Char(required=True)
    state = fields.Many2one('res.country.state',required=True)
    age = fields.Integer(required=True, default=18)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')], string='Gender', required=True)
    blood_group = fields.Many2one('blood.type', string='Blood Group')
    health_info = fields.Text(string='Health Information')
    donor_request_ids = fields.One2many('donation.request','donor_name',readonly=True)
    # donor_donation_ids = fields.One2many('donation.request','donor_request_id', readonly=True)
