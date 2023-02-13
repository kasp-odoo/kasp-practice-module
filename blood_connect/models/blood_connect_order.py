from odoo import fields,models

class BloodConnectOrder(models.Model):
    _name = "blood.connect.order"
    _description = "Blood Connect Order Model"

    order_id = fields.Char(string='Order ID', required=True)
    order_date = fields.Date(string='Order Date', required=True)
    blood_unit = fields.Integer(string='Blood Unit(s)', required=True)
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
        ], required=True) # can also done with dedicated blood group model Many2one
    name = fields.Char(string='Patient/Hospital Name', required=True)
    delivery_date = fields.Date(string='Delivery Date', required=True)
    delivery_loc = fields.Char(string='Delivery Location', required=True)
    state = fields.Selection(
        selection = [('confirmed','Confirmed'),
                     ('delivered','Delivered'),
                     ('cancelled','Cancelled')], string='State', copy=False)
    # Order Approver (Blood Bank or Donation Center Representative)