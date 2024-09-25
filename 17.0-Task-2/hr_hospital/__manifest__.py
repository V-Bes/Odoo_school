{
    'name': 'HR hospital',
    'author': 'Vladislav',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.1.1.0',

    'data': [
        'security/ir.model.access.csv',
        'data/hr.hospital.visit.csv',
        'data/hr.hospital.diseases.csv',
        'data/hr.hospital.doctor.csv',
        'data/hr.hospital.patient.csv',
        'views/hr_hospital_menu.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_visit_views.xml',

    ],
    'demo': [
        'demo/hr.hospital.doctor.csv',
        'demo/hr.hospital.patient.csv',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],
}
