from odoo import models, fields, api

class Estate_Property_tag(models.Model) :
    _name = 'estate.property.tag'
    _description = 'Property Tags'

    name = fields.Char(required=True, string='Name')
