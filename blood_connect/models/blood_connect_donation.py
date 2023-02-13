from odoo import fields,models

class BloodConnectDonation(models.Model):
    _name = "blood.connect.donation"
    _description = "Blood Connect Blood Donation Model"

    # Donor ID (Many2one)
    # Blood Group (Many2one)
    donated_quantity = fields.Float(string='Donated Qunatity(ml)',readonly=True)
    donation_date = fields.Datetime(string='Donation Date',readonly=True)
    # Donation Center (Many2one)
    # Receptionist (Many2one)
    test_results = fields.Text(string='Test Results',required=True)
    state = fields.Selection(
        selection = [('donated','Donated'),
                     ('tested','Tested'),
                     ('approved','Approved'),
                     ('rejected','Rejected')], string='State', default="donated", copy=False)
