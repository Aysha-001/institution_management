from odoo import models, fields

class Department(models.Model):
    _name = 'institution.department'
    _description = 'Department'

    name = fields.Char(string='Name', required=True)