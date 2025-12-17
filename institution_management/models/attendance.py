from odoo import models, fields

class Attendance(models.Model):
    _name = 'institution.attendance'
    _description = 'Attendance for a day'

    date = fields.Date(string='Attendance Date')

    batch_id = fields.Many2one(
        'institution.batch',
        string='Batch',
        required=True,
        ondelete='cascade'
    )

    attendance_ids = fields.One2many(
        'institution.session.attendance',
        'attendance_id',
        string='Session Attendances',
    )
