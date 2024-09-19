import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HrHospitalVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit'

    name = fields.Char()
    description = fields.Text()
