from odoo import models, fields, api
from datetime import date

class Student(models.Model):
    _name = 'institution.student'
    _description = 'Student'

    user_id = fields.Many2one('res.users', string='Related User')

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    admission_no = fields.Char(
        string='Admission No', readonly=True, copy=False, default='New')
    guardian = fields.Char(string='Guardian', required=True)
    age = fields.Integer(string='Age', compute='_compute_age')
    dob = fields.Date(string='Date of Birth', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    address = fields.Text(string='Address', required=True)

    fee_status = fields.Selection(
        [('paid','Paid'), ('unpaid','Unpaid')],
        string='Fee Status',
        compute='_compute_fee_status')

    active = fields.Boolean(default=True)

    course_id = fields.Many2one(
        'institution.course',
        string='Course enrolled',
        required=True
    )

    batch_id = fields.Many2one(
        'institution.batch',
        string='Batch',
    )

    fee_ids = fields.One2many(
        'institution.fees',
        'student_id',
        string='Fees',
    )

    _sql_constraints = [
        ('admission_no_unique',
         'unique(admission_no)',
         'No Two admission no can be same!!')
    ]

    pending_fee_ids = fields.One2many(
        'institution.fees',
        'student_id',
        string="Pending Fees",
        domain=[('payment_status', '=', 'pending')]
    )

    @api.depends('dob')
    def _compute_age(self):
        today = date.today()
        for student in self:
            student.age = today.year - student.dob.year

    #looks for multiple values
    @api.depends('fee_ids.payment_status')
    def _compute_fee_status(self):
        for student in self:
            if student.fee_ids:
                student.fee_status = 'unpaid'
                if all(fee.payment_status == 'paid' for fee in student.fee_ids):
                    student.fee_status = 'paid'
            else:
                student.fee_status = 'unpaid'

    @api.model
    def create(self, vals):
        for val in vals:
            if val.get('admission_no', 'New') == 'New':
                val['admission_no'] = self.env['ir.sequence'].next_by_code('institution.student')

        return super().create(vals)










