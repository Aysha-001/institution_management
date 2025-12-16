from odoo import models, fields


class Student(models.Model):
    _name = 'institution.student'
    _description = 'Student'


    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    admission_no = fields.Char(string='Admission No', required=True)
    guardian = fields.Char(string='Guardian', required=True)
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    address = fields.Text(string='Address', required=True)
    active = fields.Boolean(default=True)


