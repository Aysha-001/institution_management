from odoo import models, fields

class Batch(models.Model):
    _name = 'institution.batch'
    _description = 'Batch'

    name = fields.Char(string='Batch Name', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    #status
    course_id = fields.Many2one(
        'institution.course',
        string='Course')

    student_id = fields.One2many(
        'institution.student',
        'batch_id',
        string='Student',
    )

