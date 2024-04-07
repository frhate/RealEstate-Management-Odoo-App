from odoo import models, fields, api

class Hold(models.Model):
    _name = 'hold'
    _description = 'Types of hold '

    type = fields.Char(string='Type', required=True)