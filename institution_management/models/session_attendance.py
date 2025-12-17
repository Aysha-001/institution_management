from odoo import models, fields

class SessionAttendance(models.Model):
    _name = 'institution.session.attendance'
    _description = 'Attendance for each sessions'

    attendance_id = fields.Many2one(
        'institution.attendance',
        string='Attendance',
        required=True,
        ondelete='cascade'
    )

    student_id = fields.Many2one(
        'institution.student',
        string='Student',
        required=True,
        ondelete='cascade'
    )

    present = fields.Boolean(string='Present')