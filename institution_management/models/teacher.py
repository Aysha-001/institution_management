from odoo import models, fields

class Teacher(models.Model):
    _name = 'institution.teacher'
    _description = 'Teacher'
    _inherits = {'institution.staff': 'staff_id'}

    '''
    Many2one creates the link
    _inherits explains how to use the link
    
    here the relation is 1:1 composition not the generic many to one
    '''
    staff_id = fields.Many2one(
        'institution.staff',
        required=True,
        ondelete='cascade',
    )
    area_of_expertise = fields.Char(string='Area of Expertise', required=True)

    course_assigned = fields.Many2many(
        'institution.course',
        string='Course Assigned'
    )

