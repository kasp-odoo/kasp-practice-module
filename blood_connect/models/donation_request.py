# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DonationRequest(models.Model):
    _name = "donation.request"
    _description = "Blood Connect Blood Donation Request Model"

    donor_name = fields.Many2one('donor.donor', string='Donor Name', required=True)
    blood_group = fields.Many2one('blood.type', related='donor_name.blood_group', store=True, string='Blood Group')
    appointment_date = fields.Datetime(string='Appointment Date', required=True)
    center_id = fields.Many2one('donation.center', string='Donation Center', required=True)
    # donation_center = fields.Many2one('donation.center')
    center_name = fields.Char(related='center_id.name')
    donated_units = fields.Integer(string='Donated Units', default=0)
    state = fields.Selection(
        selection = [
            ('requested','Requested'),
            ('approved','Approved'),
            ('donated','Donated'),
            ('not donated','Not Donated'),
            ('rejected','Rejected')], default='requested', string="Status")

    def action_accept_donation(self):
        for record in self:
            record.state = 'approved'
        return True

    def action_reject_donation(self):
        for record in self:
            record.state = 'rejected'
        return True

    def action_donated(self):
        for record in self:
            record.state = 'donated'
        return True

    def action_not_donated(self):
        for record in self:
            record.state = 'not donated'
        return True
