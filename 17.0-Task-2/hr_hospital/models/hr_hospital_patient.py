import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'

    name = fields.Char()
    age = fields.Integer()
    description = fields.Text()

    hr_hospital_visit_id = fields.Many2one(
        comodel_name='hr.hospital.visit',
        string="Visit",
    )
    hr_hospital_diseases_ids = fields.Many2many(
        comodel_name='hr.hospital.diseases',
        string="Diseases",
    )
