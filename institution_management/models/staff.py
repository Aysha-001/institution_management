from odoo import models, fields

class Staff(models.Model):
    _name = 'institution.staff'
    _description = 'Staff'

    employee_id = fields.Char(string='Employee ID', required=True, copy=False, readonly=True, default='New')
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    age = fields.Integer(string='Age', required=True)
    dob = fields.Datetime(string='Date of Birth', required=True)
    work_email = fields.Char(string='Email', required=True)
    work_contact = fields.Char(string='Phone', required=True)
    job_title = fields.Char(string='Job Title', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', required=True)
    salary = fields.Float(string='Salary', required=True)
    marital_status = fields.Selection([('married', 'Married'),('divorced', 'Divorced'), ('single', 'Single')] , string='Marital Status' )
    department_id = fields.Many2one('institution.department', string='Department', required=True)
    date_joined = fields.Datetime(string='Date Joined', required=True)
    address = fields.Text(string='Address', required=True)
