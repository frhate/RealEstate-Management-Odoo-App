from odoo import models, fields, api

class PropertyBuilding(models.Model):
    _name = 'property.building'
    _description = 'Property Building Information'

    name = fields.Char(string='Name', required=True)
    hold_type_id = fields.Many2one('res.hold', string='Hold Type', required=True)
    project_id = fields.Many2one('res.projecto.project_info' , string='Project')
    state_id = fields.Many2one('res.country.state', string='State', required=True, ondelete='cascade')
    city_id = fields.Many2one('res.city', string='City', required=True, ondelete='cascade')
    land_no_id = fields.Char(string='Land No')
    municipality_no = fields.Char(string='Municipality No')

    # Building Names
    building_name = fields.Char(string='Building Name', required=True)
    arabic_name = fields.Char(string='Arabic Name', required=True)

    # Ejari Details
    ejari_building_name = fields.Char(string='Ejari Building Name', required=True)
    ejari_building_name_arabic = fields.Char(string='Ejari Arabic Name', required=True)
    ejari_building_area_size = fields.Float(string='Ejari Building Area Size', required=True)
    ejari_common_area_size = fields.Float(string='Ejari Common Area Size', required=True)
    ejari_leasable_area_size = fields.Float(string='Ejari Leasable Area Size', required=True)

    address = fields.Char(string='Address', required=True)
    unit_count = fields.Integer(string='Unit Count')
    completion_date = fields.Date(string='Completion Date')

    building_usage_ids = fields.Many2many(comodel_name='building.usage', string='Building Usage', required=True)
    building_type_id = fields.Many2one(comodel_name='building.type', string='Building Type', required=True)

    floor_count = fields.Integer(string='Floor Count')
    parking_count = fields.Integer(string='Parking Count')
    buid_area_size = fields.Float(string='Building Area Size')
    plot_area_size = fields.Float(string='Plot Area Size')
    leasable_area_size = fields.Float(string='Leasable Area Size')
    commom_area_size = fields.Float(string='Common Area Size')

    status = fields.Selection(string='Status', selection=[('approved', 'Approved'),('not_approved', 'Not Approved')])  # Replace with your specific status options
    reference_number = fields.Char(string='Reference Number')
    approval_ref_no = fields.Char(string='Approval Reference No')
    active = fields.Boolean(string='Active', default=True)


