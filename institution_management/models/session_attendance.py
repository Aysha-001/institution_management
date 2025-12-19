from odoo import models, fields, api

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

    present_int = fields.Integer(
        string='Present count',
        compute='_compute_present',
        store=True,
    )

    attendance_date = fields.Date(
        related='attendance_id.date',
        store=True,
        string='Attendance Date'
    )

    @api.depends('present')
    def _compute_present(self):
        for record in self:
            record.present_int = 1 if record.present else 0
