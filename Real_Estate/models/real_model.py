from odoo import models, fields, api
# from odoo.exceptions import ValidationError

class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description', help='Enter Importance Details')
    postcode = fields.Char(string='PostCode')
    date_availability = fields.Date(string='Available From')
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(selection=[
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West'),
    ])
    active = fields.Boolean(default=True, string='Active')
    status = fields.Selection(selection=[
        ('New', 'New'),
        ('Offer Received', 'Offer Received'),
        ('Offer Accepted', 'Offer Accepted')
    ], default='New', string='Status')

    search = fields.Char(string='Search')

    # @api.constrains('expected_price')
    # def _Check_email_Field_Value_Exist(self):
    #     for rec in self :
    #         print('req :- ', rec)
    #         if rec.expected_price is None or rec.expected_price <= 10:
    #             raise ValidationError('Not Found')

