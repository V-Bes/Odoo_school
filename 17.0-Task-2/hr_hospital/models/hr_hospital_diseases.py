import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalDiseases(models.Model):
    _name = 'hr.hospital.diseases'
    _description = 'Diseases'

    name = fields.Char()
    hr_hospital_patient_ids = fields.Many2many(
        comodel_name='hr.hospital.patient',
        string='Diseases',
    )
