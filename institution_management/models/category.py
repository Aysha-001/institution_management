from odoo import models, fields

class Category(models.Model):
    _name = 'institution.category'
    _description = 'Institution Category'

    name = fields.Char(string='Name')
