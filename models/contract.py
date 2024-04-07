from odoo import models, fields

class PropertyContract(models.Model):
    _name = 'property.contract'
    _description = 'Property Contract'

    name = fields.Char(string='Name', required=True)
    stage_id = fields.Many2one('stage.model', string='Stage')
    kanban_state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done'),
    ], string='Kanban State')
    active = fields.Boolean(default=True)
    code = fields.Char(string='Code')
    company_id = fields.Many2one('res.company', string='Company')
    partner_id = fields.Many2one('res.partner', string='Partner')
    user_id = fields.Many2one('res.users', string='User')
    date = fields.Date(string='Date')
    date_start = fields.Date(string='Start Date')
    date_stop = fields.Date(string='End Date')
    period = fields.Date(string='Period')
    period_nbr = fields.Integer(string='Period Number')
    currency_id = fields.Many2one('res.currency', string='Currency')
    value = fields.Float(string='Value')
    notes = fields.Text(string='Notes')