from odoo import models, fields, api
from datetime import date


class Batch(models.Model):
    _name = 'institution.batch'
    _description = 'Batch'

    name = fields.Char(string='Batch Name', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    status = fields.Selection(
        [('completed','Completed'),('ongoing','Ongoing')],
        string='Status',
        compute='_compute_status',
        store=True)

    course_id = fields.Many2one(
        'institution.course',
        string='Course')

    student_id = fields.One2many(
        'institution.student',
        'batch_id',
        string='Student',
    )

    @api.depends('end_date')
    def _compute_status(self):
        today = date.today()
        for batch in self:
            if batch.end_date < today:
                batch.status = 'completed'
            else:
                batch.status = 'ongoing'



