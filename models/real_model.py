from odoo import models, fields, api
from datetime import datetime

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

    property_selection = fields.Selection(selection=[
        ('House','House'),
        ('Apartment','Apartment')
    ], default='House')

    property_type_id = fields.Many2one("property.type", string="Property Type")
    salesperson_name = fields.Char(string="Salesperson", compute='_compute_salesperson_name', store=False)
    buyer_name = fields.Char(string="Buyer", compute='_compute_buyer_name', store=False)

    tag_ids = fields.Many2many("estate.property.tag", string='Property Tag')
    offer_ids = fields.One2many('estate.property.offer','property_id')

    total_area = fields.Integer(string='Total Area', compute='_compute_total_area')
    best_price = fields.Integer(string='Best Price', compute='_compute_best_price')

    @api.depends('property_type_id.salesperson_id')
    def _compute_salesperson_name(self):
        for record in self:
            record.salesperson_name = record.property_type_id.salesperson_id.name if record.property_type_id and record.property_type_id.salesperson_id else "No Salesman"

    @api.depends('property_type_id.buyer_id')
    def _compute_buyer_name(self):
        for record in self:
            record.buyer_name = record.property_type_id.buyer_id.name if record.property_type_id and record.property_type_id.buyer_id else "No Buyer"

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self :
            record.total_area = record.living_area + record.garden_area if record.living_area and record.garden_area else 0

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            prices = record.offer_ids.mapped('price')
            record.best_price = max(prices) if prices else 0.0

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

    salesperson_id = fields.Many2one(
        'res.users',
        string="Salesman",
        default=lambda self: self.env.user
    )

class Estate_Property_tag(models.Model) :
    _name = 'estate.property.tag'
    _description = 'Property Tags'

    name = fields.Char(required=True, string='Name')

class Estate_Property_Offer(models.Model) :
    _name = 'estate.property.offer'
    _description = 'Property Offer'

    price = fields.Float(string='Price')
    status = fields.Selection(selection=[('Accepted','Accepted'),('Refused','Refused')], string='Status', copy=False, default='Accepted')
    partner_id = fields.Many2one(
        'res.partner',
        string='Partner',
        required=True,
        default=lambda self: self.env.ref('base.res_partner_2', raise_if_not_found=False)
    )
    property_id = fields.Many2one(
        'real.estate.property',
        string='Property id',
        required=True
    )
    validity = fields.Integer(default=7, string='Validity (days)')
    date_deadline = fields.Date(compute='_compute_date_deadline')

    @api.depends('validity','create_date')
    def _compute_date_deadline(self):
        for record in self :
            pass