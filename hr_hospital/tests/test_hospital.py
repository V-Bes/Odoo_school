import logging
from datetime import timedelta
from odoo import fields
from odoo.exceptions import ValidationError, UserError
from .common import TestCommon

_logger = logging.getLogger(__name__)


class TestVisitConstraints(TestCommon):

    def test_01_action_visit_duplicate(self):
        with self.assertRaises(ValidationError):
            self.test_visit2.write({
                'hr_hospital_patient_id': self.test_patient.id,
                'hr_hospital_doctor_id': self.test_doctor.id,
                'planned_date': self.test_visit1.planned_date,
            })

    def test_02_action_patient_age(self):
        self.assertTrue(int(self.test_patient.age) > 0)

    def test_03_action_doctor_mentor(self):
        with self.assertRaises(ValidationError):
            self.test_doctor.write({
                'mentor_id': self.test_doctor.id,
            })
