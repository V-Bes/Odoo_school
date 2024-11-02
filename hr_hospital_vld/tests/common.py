from odoo import fields
from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()

        self.test_patient = self.env['hr.hospital.patient'].create({
            'first_name': 'Test_patient',
            'last_name': 'Test_patient',
            'birthday': '2000-01-01',
        })

        self.test_doctor = self.env['hr.hospital.doctor'].create({
            'first_name': 'Test_doctor',
            'last_name': 'Test_doctor',
        })

        self.test_visit1 = self.env['hr.hospital.visit'].create({
            'hr_hospital_patient_id': self.test_patient.id,
            'hr_hospital_doctor_id': self.test_doctor.id,
            'planned_date': fields.Datetime.now(),
        })

        self.test_visit2 = self.env['hr.hospital.visit'].create({
        })
