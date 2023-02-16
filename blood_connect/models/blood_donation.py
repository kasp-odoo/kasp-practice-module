# -*- coding: utf-8 -*-
from odoo import fields, models


class BloodDonation(models.Model):
    _name = "blood.donation"
    _description = "Blood Connect Blood Donation Model"

    donor_name = fields.Many2one('donor.donor', string='Donor Name')
    # donation_request_date = fields.Date(string='Donation Request')
    blood_group = fields.Many2one('blood.type', string='Blood Group')
    donated_quantity = fields.Float(string='Donated Qunatity(ml)', readonly=True)
    donation_date = fields.Datetime(string='Donation Date', readonly=True)
    donation_center = fields.Many2one('donation.center', string='Donation Center')
    # Receptionist (Many2one)
    test_results = fields.Text(string='Test Results', required=True)
    state = fields.Selection(
        selection=[('requested', 'Requested'),
                   ('donated', 'Donated'),
                   ('tested', 'Tested'),
                   ('approved', 'Approved'),
                   ('rejected', 'Rejected')], string='State', default="donated", copy=False)
