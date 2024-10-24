{
    'name': 'HR hospital',
    'author': 'Vladislav',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.1.1.0',

    'data': [
        'security/ir.model.access.csv',
        'data/hr.hospital.visit.xml',
        'data/hr.hospital.doctor.csv',
        'data/hr.hospital.patient.csv',
        'data/hr.hospital.disease.xml',
        'data/hr.hospital.diagnosis.csv',
        'wizard/hr_group_change_patient_wizard_view.xml',
        'wizard/report_disease_wizard_view.xml',
        'report/hr_hospital_doctor_report.xml',
        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_visit_views.xml',
        'views/hr_hospital_disease_views.xml',
        'views/hr_hospital_diagnosis_views.xml',
        'views/hr_hospital_patient_views.xml',
        'wizard/view_visits_patient_wizard_view.xml',
        'report/hr_hospital_disease_report.xml',

    ],
    'demo': [
        'demo/hr.hospital.visit.xml',
        'demo/hr.hospital.doctor.csv',
        'demo/hr.hospital.patient.csv',
        'demo/hr.hospital.disease.xml',
        'demo/hr.hospital.diagnosis.csv',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],
}
