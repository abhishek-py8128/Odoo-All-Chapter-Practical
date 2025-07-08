from odoo import models, fields, api
from datetime import datetime

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

    property_type_id = fields.Many2one(
        'property.type',
        string='Property id',
    )
    validity = fields.Integer(default=7, string='Validity (days)')
    date_deadline = fields.Date()

    @api.depends('validity','create_date')
    def _compute_date_deadline(self):
        for record in self :
            pass