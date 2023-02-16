# -*- coding: utf-8 -*-
from odoo import fields, models


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
    # Blood Stock (One2many)
    # Orders (One2many)

# Patient Blood Requests Page (One2many)
# Add Orders page (One2many)

# City: The city in which the hospital is located
# State: The state or province in which the hospital is located
# Country: The country in which the hospital is located
# Zip code: The zip or postal code of the hospital's location
# Phone number: The hospital's phone number
# Email: The hospital's email address
# Contact person: The name of the person who should be contacted for inquiries or emergencies
# Website: The hospital's website, if it has one.