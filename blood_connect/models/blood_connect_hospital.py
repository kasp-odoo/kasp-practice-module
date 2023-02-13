from odoo import fields,models

class BloodConnectHospital(models.Model):
    _name = "blood.connect.hospital"
    _description = "Blood Connect Hospital Model"

    name = fields.Char(string='Hospital Name', required=True)
    contact = fields.Char(string='Contact Number', required=True)
    address = fields.Char(string='Address', required=True)
    donation_center = fields.Boolean(string='Does hospital has donation center ?')
    # Blood Stock (One2many)
    # hospital ID ()
    # Orders (One2many)
    # Appointments (One2many)