import logging

from odoo import models, fields


_logger = logging.getLogger(__name__)


class HrHospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _inherit = ['human.mixin',]
    _description = 'Patient'
    _rec_name = 'last_name'

    birthday = fields.Date()
    age = fields.Integer(
        compute='_compute_age'
    )

    passport = fields.Text()

    contact = fields.Char()

    hr_hospital_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string="Doctor",
    )

    visits_ids = fields.One2many(
        comodel_name='hr.hospital.visit',
        inverse_name='hr_hospital_patient_id',
    )

    hr_hospital_diagnosis_ids = fields.One2many(
        compute='_compute_diagnosis',
        comodel_name='hr.hospital.diagnosis',
        inverse_name='hr_hospital_patient_id',
    )

    def _compute_diagnosis(self):
        for record in self:
            diagnosis_ids = self.env['hr.hospital.diagnosis']
            for visit in record.visits_ids:
                diagnosis_ids |= visit.hr_hospital_diagnosis_ids
            record.hr_hospital_diagnosis_ids = diagnosis_ids

    color = fields.Integer(string='Color Index')

    def test_button(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': 'Test button clicked!',
                'type': 'info',
                'sticky': False,
            }
        }

    def _compute_age(self):
        for record in self:
            if record.birthday:
                record.age = fields.Date.today().year - record.birthday.year
            else:
                record.age = 0
