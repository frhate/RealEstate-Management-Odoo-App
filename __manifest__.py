# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Contract Manager',
    'version': '1.0',
    'category': 'Administration',
    'summary': 'Immobile Contract Manager',
    'depends': ['base'],
    'data': ['views/project_forms.xml',
             'views/building_forms.xml' ,
             'views/units_forms.xml',
             'views/contract_froms.xml',
             'views/contract_menus.xml',
             'security/ir.model.access.csv' ],

    'installable': True,
    'license': 'LGPL-3',
}