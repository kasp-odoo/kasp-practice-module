# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Hospital(models.Model):
    _name = "hospital.hospital"
    _description = "Blood Connect Hospital Model"

    name = fields.Char(string='Hospital Name', required=True)
    address = fields.Char(string='Address', required=True)
    city = fields.Char(required=True)
    state = fields.Many2one('res.country.state',required=True)
    zip_code = fields.Char(string='Zip Code', required=True)
    contact = fields.Char(string='Contact Number', required=True)
    website = fields.Char()
    blood_request_ids = fields.One2many('blood.request','hospital_name')