# -*- coding: utf-8 -*-
from odoo import fields,models

class BloodConnectRequest(models.Model):
    _name = "blood.connect.request"
    _description = "Blood Connect Requests Model"

    request_by = fields.Selection(
        selection = [
            ('patient','Patient'),
            ('hospital','Hospital'),
        ], required=True, string='Request By', default='Patient')
    name = fields.Char(required=True)
    address = fields.Text(required=True)
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
        ], required=True) # Can also done with blood_group model
    quantity = fields.Integer(required=True, string='Required Blood Units', default=1)
    date = fields.Date(string='Request Date',default=lambda self: fields.Date.today())
    state = fields.Selection(
        selection = [('new','New'),
                     ('pending','Pending'),
                     ('fulfilled','Fulfilled'),
                     ('canceled','Canceled')], string='State', default="new", copy=False)

    
    
    