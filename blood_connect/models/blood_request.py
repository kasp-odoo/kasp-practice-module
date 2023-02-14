# -*- coding: utf-8 -*-
from odoo import fields, models


class BloodRequest(models.Model):
    _name = "blood.request"
    _description = "Blood Connect Requests Model"

    request_by = fields.Selection(
        selection=[
            ('patient', 'Patient'),
            ('hospital', 'Hospital'),
        ], required=True, string='Request By', default='Patient')
    name = fields.Char(required=True)
    address = fields.Text(required=True)
    blood_group = fields.Many2one('blood.type', string='Blood Group')
    quantity = fields.Integer(
        required=True, string='Required Blood Units', default=1)
    date = fields.Date(string='Request Date',
                       default=lambda self: fields.Date.today())
    state = fields.Selection(
        selection=[('new', 'New'),
                   ('pending', 'Pending'),
                   ('fulfilled', 'Fulfilled'),
                   ('cancelled', 'Cancelled')], string='State', default="new", copy=False)
