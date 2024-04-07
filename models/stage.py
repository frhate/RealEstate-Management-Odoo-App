from odoo import models, fields

class PropertyStage(models.Model):
    _name = 'property.stage'
    _description = 'Property stage'

    name = fields.Char(string='Name', required=True)