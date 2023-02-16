# -*- coding: utf-8 -*-
from odoo import fields, models


class DonationRequest(models.Model):
    _name = "donation.request"
    _description = "Blood Connect Blood Donation Request Model"

    donor_name = fields.Many2one('donor.donor', string='Donor Name', required=True)
    blood_group = fields.Many2one('blood.type', string='Blood Group', required=True)
    appointment_date = fields.Date(string='Appointment Date', required=True)
    donation_center = fields.Many2one('donation.center', string='Donation Center', required=True)
    status = fields.Selection(
        selection = [
            ('pending','Pending'),
            ('approved','Approved'),
            ('rejected','Rejected')], default='pending')