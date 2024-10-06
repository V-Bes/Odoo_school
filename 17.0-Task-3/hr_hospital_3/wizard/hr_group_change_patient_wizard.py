import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HrGroupChangePatient(models.TransientModel):
    _name = 'hr.group.change.patient.wizard'
    _description = 'Group change patient.'

    patient_ids = fields.Many2many(
        comodel_name='hr.hospital.patient',
        readonly=True,
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
    )

    def add_reader(self):
        self.patient_ids.hr_hospital_doctor_id = self.doctor_id