import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

CONST_EXP = "example"


class HrHospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'

    name = fields.Char()
    description = fields.Text()
    active = fields.Boolean(
        default=True,
    )
