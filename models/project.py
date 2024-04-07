from odoo import models, fields

class Project_info(models.Model):
    _name = 'projecto.project_info'
    _description = 'Project Information'

    name = fields.Char(string='Project Name', required=True)
    owner = fields.Many2one('res.partner', string='Owner')
    managed_by = fields.Many2one('res.partner', string='Managed By')
    maintained_by = fields.Many2one('res.partner', string='Maintained By')
    active = fields.Boolean(string='Active', default=True)
    emirate = fields.Selection([
        ('abu_dhabi', 'Abu Dhabi'),
        ('dubai', 'Dubai'),
        ('sharjah', 'Sharjah'),
        ('ajman', 'Ajman'),
        ('um_al_quwain', 'Umm Al Quwain'),
        ('fujairah', 'Fujairah'),
        ('rak', 'Ras Al Khaimah'),
    ], string='Emirate')
    area = fields.Char(string='Area')  # Project area

    # Add missing fields
    hold_type_id = fields.Many2one('hold.type', string='Hold Type')
    city_id = fields.Many2one('res.city', string='City')
    building_usage_ids = fields.Many2many('building.usage', string='Building Usage')
    building_type_id = fields.Many2one('building.type', string='Building Type')
