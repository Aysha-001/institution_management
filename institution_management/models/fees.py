from odoo import models, fields ,api

class Fees(models.Model):
    _name = 'institution.fees'
    _description = 'Student Fees'

    amount = fields.Float(string='Amount', required=True)

    due_date = fields.Date(string='Due Date', required=True)
    payment_date = fields.Date(string='Payment Date')

    student_id = fields.Many2one(
        'institution.student',
        string='Student',
        required=True,
        ondelete='cascade',
    )

    payment_status = fields.Selection([('paid', 'Paid'),('pending', 'Pending')], default='pending')


