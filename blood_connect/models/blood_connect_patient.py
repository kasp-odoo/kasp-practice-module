from odoo import fields,models

class BloodConnectPatient(models.Model):
    _name = "blood.connect.patient"
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
    # patient ID
    health_info = fields.Text(string='Health Information (Reason)', required=True)
