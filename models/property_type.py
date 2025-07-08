from odoo import models, fields, api

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
