from odoo import models, fields

class Unit(models.Model):
    _name = 'property.unit'
    _description = 'The Property Units'

    name = fields.Char(string='Name', required=True)
    unit_no = fields.Char(string='Unit Number', required=True)
    suit_area_size = fields.Float(string='Suit Area Size', required=True)
    common_area_size = fields.Float(string='Common Area Size', required=True)
    approval_ref_no = fields.Selection([('no', 'No'), ('yes', 'Yes')], string='Approval Ref', required=True)
    Floor_no = fields.Float(string='Floor No', required=True)
    status = fields.Selection([('draft', 'Draft')])
    total_area_size = fields.Float(string='Total Area')
    reference_no = fields.Char(string='Reference No')
