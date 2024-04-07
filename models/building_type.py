from odoo import models, fields

class Propertytype(models.Model):
    _name = 'property.type'
    _description = 'Property type'

    name = fields.Char(string='Name', required=True)