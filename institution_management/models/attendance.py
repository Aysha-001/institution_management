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

        #self.env - gateway to db
        students = self.env['institution.student'].search([
            ('batch_id', '=' , self.batch_id.id)
        ])

        lines = []

        for student in students:
            line_value = (0,0,{
                'student_id': student.id,
                'present' : True,
            })
            lines.append(line_value)
            #get students of batch
            #get institution.batch.student_id
            #insert them as editable lines
        self.attendance_ids = lines

