import logging
from email.policy import default

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalDiseases(models.Model):
    _name = 'hr.hospital.diseases'
    _description = 'Diseases'

    name = fields.Char()
    description = fields.Text()
    approved = fields.Boolean(
        default=False
    )
    hr_hospital_visit_id = fields.Many2one(
        comodel_name='hr.hospital.visit',
        string="Visit",
    )
