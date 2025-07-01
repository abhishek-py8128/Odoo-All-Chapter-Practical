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

    property_type_id = fields.Many2one("property.type", string="PropertyType")

    salesperson_name = fields.Char(string="Salesperson", compute='_compute_salesperson_name', store=False)
    buyer_name = fields.Char(string="Buyer", compute='_compute_buyer_name', store=False)

    @api.depends('property_type_id.salesperson_id')
    def _compute_salesperson_name(self):
        for record in self:
            record.salesperson_name = record.property_type_id.salesperson_id.name if record.property_type_id and record.property_type_id.salesperson_id else "No Salesman"

    @api.depends('property_type_id.buyer_id')
    def _compute_buyer_name(self):
        for record in self:
            record.buyer_name = record.property_type_id.buyer_id.name if record.property_type_id and record.property_type_id.buyer_id else "No Buyer"

class PropertyType(models.Model) :
    _name = 'property.type'
    _description = 'Property Type'

    name = fields.Char(required=True, string='Property Type')

    buyer_id = fields.Many2one(
        'res.partner',
        string="Buyer",
        copy=False,
        default=lambda self: self.env.ref('base.res_partner_2', raise_if_not_found=False)  # Optional static partner
    )

    # Salesperson (linked to res.users)
    salesperson_id = fields.Many2one(
        'res.users',
        string="Salesman",
        default=lambda self: self.env.user  # Current logged-in user
    )
