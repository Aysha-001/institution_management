from odoo import models, fields

class Batch(models.Model):
    _name = 'institution.batch'
    _description = 'Batch'

    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    #status
    course_id = fields.Many2one(
        'institution.course',
        string='Course',
        required=True)

    student_id = fields.One2many(
        'institution.student',
        'batch_id',
        string='Student',
    )