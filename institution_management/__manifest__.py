{
'name': 'Institution Management',
'version': '1.0',
'summary': 'Simple module to manage students',
'description': 'Minimal module that allows creating Student records',
'author': 'You',
'category': 'Education',
'depends': ['base'],
'data': [
    'views/student_views.xml',
    'views/staff_views.xml',
    'views/department_views.xml',
    'security/ir.model.access.csv',
],
'installable': True,
'application': True,
}