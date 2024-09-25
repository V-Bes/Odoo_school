import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit'

    name = fields.Char()
    planned_date = fields.Datetime()
    visit_date = fields.Datetime()
    status_visit = fields.Selection(
        string='Status',
        selection=[
            ('planned','planned'),
            ('completed','completed'),
            ('cancel','cancel'),
        ],
    )

    hr_hospital_doctor_id = fields.Many2one(
       comodel_name='hr.hospital.doctor',
       string="Doctor",
    )

    hr_hospital_patient_id = fields.Many2one(
       comodel_name='hr.hospital.patient',
       string="Patient",
    )

    hr_hospital_diseases_ids = fields.One2many(
       comodel_name='hr.hospital.diseases',
       inverse_name='hr_hospital_visit_id',
       string="Diseases",
    )
