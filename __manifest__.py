# -*- coding: utf-8 -*-
{
    'name': 'Pharmacy Managment',
    'version': '1.0.0',
    'category': 'Healthcare',
    'summary': 'pharmacy managment system',
    'author': 'Aya Ahmed',
    'description': """pharmacy managment system""",
    'sequence':-100,
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml'
    ],
    'demo': [],
    'application':True,
    'auto_install': False,
    'license': 'LGPL-3',
}
