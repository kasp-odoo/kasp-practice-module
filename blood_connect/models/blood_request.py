# -*- coding: utf-8 -*-
from odoo import fields, models


class BloodRequest(models.Model):
    _name = "blood.request"
    _description = "Blood Connect Requests Model"

    request_by = fields.Selection(
        selection=[
            ('patient', 'Patient'),
            ('hospital', 'Hospital'),
        ], required=True, string='Request By', default='patient')
    # name = fields.Char(required=True)
    patient_name = fields.Many2one('patient.patient')
    hospital_name = fields.Many2one('hospital.hospital')
    # address = fields.Text(required=True)
    blood_group = fields.Many2one('blood.type', string='Blood Group', required=True)
    quantity = fields.Integer(required=True, string='Required Blood Units', default=1)
    # city = fields.Char()
    # select_state = fields.Many2one('res.country.state', required=True)
    order_id = fields.Many2one('donation.center')
    date = fields.Date(string='Request Date', default=lambda self: fields.Date.today(), required=True)
    requested_from = fields.Many2one('donation.center', required=True)
    state = fields.Selection(
        selection=[('new', 'New'),
                   ('approved', 'Approved'),
                   ('cancelled', 'Cancelled')], default="new", copy=False)
