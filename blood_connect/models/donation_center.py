# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class DonationCenter(models.Model):
    _name = "donation.center"
    _description = "Blood Connect Donation Center Model"

    _sql_constraints = [
        ('check_capacity','CHECK(capacity > 0)','Blood unit storage capacity must be greater than 0.')
    ] 

    name = fields.Char(string='Center Name', required=True)
    address = fields.Char(required=True)
    city = fields.Char(required=True)
    state = fields.Many2one('res.country.state',required=True)
    zip_code = fields.Char(string='Zip Code', required=True)
    contact = fields.Char(string='Contact Number', required=True)
    email = fields.Char()
    capacity = fields.Integer(string='Capacity(Units)', required=True)
    order_ids = fields.One2many('blood.request','order_id')
    donation_ids = fields.One2many('donation.request','center_id')

    a_positive = fields.Integer(string='A+', default=0, compute='_compute_a_positive')
    b_positive = fields.Integer(string='B+', default=0, compute='_compute_b_positive')
    ab_positive = fields.Integer(string='AB+', default=0, compute='_compute_ab_positive')
    o_positive = fields.Integer(string='O+', default=0, compute='_compute_o_positive')
    a_negative = fields.Integer(string='A-', default=0, compute='_compute_a_negative')
    b_negative = fields.Integer(string='B-', default=0, compute='_compute_b_negative')
    ab_negative = fields.Integer(string='AB-', default=0, compute='_compute_ab_negative')
    o_negative = fields.Integer(string='O-', default=0, compute='_compute_o_negative')

    @api.depends('donation_ids','order_ids')
    def _compute_a_positive(self):
        for record in self:
            a_positive_donations = record.donation_ids.filtered(lambda d: d.blood_group.blood_type == 'A+')
            a_positive_orders = record.order_ids.filtered(lambda o: o.blood_group.blood_type == 'A+' and o.state == 'approved')
            record.a_positive = sum(a_positive_donations.mapped('donated_units')) - sum(a_positive_orders.mapped('quantity'))

    @api.depends('donation_ids','order_ids')
    def _compute_o_positive(self):
        for record in self:
            o_positive_donations = record.donation_ids.filtered(lambda d: d.blood_group.blood_type == 'O+')
            o_positive_orders = record.order_ids.filtered(lambda o: o.blood_group.blood_type == 'O+' and o.state == 'approved')
            record.o_positive = sum(o_positive_donations.mapped('donated_units')) - sum(o_positive_orders.mapped('quantity'))

    @api.depends('donation_ids','order_ids')
    def _compute_b_positive(self):
        for record in self:
            b_positive_donations = record.donation_ids.filtered(lambda d: d.blood_group.blood_type == 'B+')
            b_positive_orders = record.order_ids.filtered(lambda o: o.blood_group.blood_type == 'B+' and o.state == 'approved')
            record.b_positive = sum(b_positive_donations.mapped('donated_units')) - sum(b_positive_orders.mapped('quantity'))

    @api.depends('donation_ids','order_ids')
    def _compute_ab_positive(self):
        for record in self:
            ab_positive_donations = record.donation_ids.filtered(lambda d: d.blood_group.blood_type == 'AB+')
            ab_positive_orders = record.order_ids.filtered(lambda o: o.blood_group.blood_type == 'AB+' and o.state == 'approved')
            record.ab_positive = sum(ab_positive_donations.mapped('donated_units')) - sum(ab_positive_orders.mapped('quantity'))

    @api.depends('donation_ids','order_ids')
    def _compute_a_negative(self):
        for record in self:
            a_negative_donations = record.donation_ids.filtered(lambda d: d.blood_group.blood_type == 'A-')
            a_negative_orders = record.order_ids.filtered(lambda o: o.blood_group.blood_type == 'A-' and o.state == 'approved')
            record.a_negative = sum(a_negative_donations.mapped('donated_units')) - sum(a_negative_orders.mapped('quantity'))

    @api.depends('donation_ids','order_ids')
    def _compute_o_negative(self):
        for record in self:
            o_negative_donations = record.donation_ids.filtered(lambda d: d.blood_group.blood_type == 'O-')
            o_negative_orders = record.order_ids.filtered(lambda o: o.blood_group.blood_type == 'O-' and o.state == 'approved')
            record.o_negative = sum(o_negative_donations.mapped('donated_units')) - sum(o_negative_orders.mapped('quantity'))

    @api.depends('donation_ids','order_ids')
    def _compute_ab_negative(self):
        for record in self:
            ab_negative_donations = record.donation_ids.filtered(lambda d: d.blood_group.blood_type == 'AB-')
            ab_negative_orders = record.order_ids.filtered(lambda o: o.blood_group.blood_type == 'AB-' and o.state == 'approved')
            record.ab_negative = sum(ab_negative_donations.mapped('donated_units')) - sum(ab_negative_orders.mapped('quantity'))

    @api.depends('donation_ids','order_ids')
    def _compute_b_negative(self):
        for record in self:
            b_negative_donations = record.donation_ids.filtered(lambda d: d.blood_group.blood_type == 'B-')
            b_negative_orders = record.order_ids.filtered(lambda o: o.blood_group.blood_type == 'B-' and o.state == 'approved')
            record.b_negative = sum(b_negative_donations.mapped('donated_units')) - sum(b_negative_orders.mapped('quantity'))

