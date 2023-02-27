# -*- coding: utf-8 -*-
from odoo import api, fields, models


class BloodRequest(models.Model):
    _name = "blood.request"
    _description = "Blood Connect Requests Model"

    request_by = fields.Selection(
        selection=[
            ('patient', 'Patient'),
            ('hospital', 'Hospital'),
        ], required=True, string='Request By', default='patient')
    patient_name = fields.Many2one('patient.patient')
    hospital_name = fields.Many2one('hospital.hospital')
    blood_group = fields.Many2one('blood.type', related='patient_name.blood_group', store=True, string='Blood Group', required=True, readonly=False) # compute='_compute_blood_group'
    quantity = fields.Integer(required=True, string='Required Blood Units', default=1)
    order_id = fields.Many2one('donation.center', string='Ordered From')
    date = fields.Date(string='Request Date', default=lambda self: fields.Date.today(),readonly=True,)
    # requested_from = fields.Many2one('donation.center', required=True, default=lambda self:)
    center_name = fields.Char(related='order_id.name')
    state = fields.Selection(
        selection=[('requested', 'Requested'),
                   ('approved', 'Approved'),
                   ('cancelled', 'Cancelled')], string="Status", default="requested", copy=False)

    # @api.depends('request_by','patient_name')
    # def _compute_blood_group(self):
    #     for record in self:
    #         if(record.request_by == 'patient'):
    #             record.blood_group = record.patient_name.mapped("blood_group")[:1]
    #         else:
    #             record.blood_group = False