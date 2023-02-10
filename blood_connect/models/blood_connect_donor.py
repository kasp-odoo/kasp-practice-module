from odoo import fields,models

class BloodConnectDonor(models.Model):
    _name = "blood.connect.donor"
    _description = "Blood Connect Donor Model"

    name = fields.Char(string='Donor Name', required=True)
    phone = fields.Char(string='Phone Number', required=True)
    address = fields.Char(string='Address', required=True)
    age = fields.Integer(required=True, default=18)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', required=True)
    blood_group = fields.Selection(
        selection = [
            ('a+','A+'),
            ('o+','O+'),
            ('b+','B+'),
            ('ab+','AB+'),
            ('a-','A-'),
            ('o-','O-'),
            ('b-','B-'),
            ('ab-','AB-'),
        ], required=True)
    # donor ID
    health_info = fields.Text(string='Health Information')
