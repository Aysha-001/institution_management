from odoo import models, fields

class Course(models.Model):
    _name = 'institution.course'
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    descr = fields.Char(string='Description', required=True)
    duration = fields.Integer(string='Duration', required=True)

    assigned_teacher = fields.Many2many(
        'institution.teacher',
        string='Assigned Teacher',
    )
    categories_id = fields.Many2many(
        'institution.category',
        string='Categories',
    )

    student_ids = fields.One2many(
        'institution.student',
        'course_id',
        string='Students')

    batch_id = fields.One2many(
        'institution.batch',
        'course_id',
        string='Batches'
    )
    
