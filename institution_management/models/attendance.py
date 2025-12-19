from odoo import models, fields, api

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

    @api.onchange('batch_id')
    def load_students_of_batch(self):
        #clear existing lines
        self.attendance_ids = [(5,0,0)]

        #using command tuples
        lines = [(0,0,{'student_id': s.id, 'present': True}) for s in self.batch_id.student_id]

        self.attendance_ids = lines

