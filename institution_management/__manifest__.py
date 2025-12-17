{
'name': 'Institution Management',
'version': '1.0',
'summary': 'Simple module to manage students',
'description': 'Minimal module that allows creating Student records',
'author': 'You',
'category': 'Education',
'depends': ['base'],
'data': [
    'security/ir.model.access.csv',
    'views/student_views.xml',
    'views/staff_views.xml',
    'views/department_views.xml',
    'views/course_views.xml',
    'views/category_views.xml',
    'views/teacher_views.xml',
    'views/batch_views.xml',
    'views/fees_views.xml',
    'views/attendance_views.xml',
    'views/menu_view.xml'
],
'installable': True,
'application': True,
}