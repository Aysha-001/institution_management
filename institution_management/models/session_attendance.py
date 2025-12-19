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

    student_name = fields.Char(
        string="Student name",
        related="student_id.first_name",
        store=True
    )

    attendance_rate = fields.Float(
        string="Attendance %",
        compute="_compute_attendance_rate",
        group_operator="avg",
        store=True
    )

    @api.depends('present_int')
    def _compute_attendance_rate(self):
        for record in self:
            record.attendance_rate = 100.0 if record.present_int == 1 else 0.0

    @api.depends('present')
    def _compute_present(self):
        for record in self:
            record.present_int = 1 if record.present else 0
