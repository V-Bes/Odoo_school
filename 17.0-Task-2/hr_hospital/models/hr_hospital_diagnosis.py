import logging

from odoo import models, fields, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HrHospitalDiagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()
    description = fields.Text()
    approved = fields.Boolean(
        default=False
    )

    hr_hospital_visit_id = fields.Many2one(
        comodel_name='hr.hospital.visit',
        string="Visit",
    )

    hr_hospital_disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string="Disease",
    )

    @api.onchange('approved')
    def _onchange_approved(self):
        if (self.approved
                and self.hr_hospital_visit_id.hr_hospital_doctor_id.is_intern):
            raise ValidationError('The intern cannot confirm the diagnosis.')
