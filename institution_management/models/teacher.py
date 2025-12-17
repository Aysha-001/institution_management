from odoo import models, fields

class Teacher(models.Model):
    _inherit = 'institution.staff'
    _name = 'institution.teacher'
    _description = 'Teacher'

    area_of_expertise = fields.Char(string='Area of Expertise', required=True)
    course_assigned = fields.Many2many(
        'institution.course',
        string='Course Assigned'
    )