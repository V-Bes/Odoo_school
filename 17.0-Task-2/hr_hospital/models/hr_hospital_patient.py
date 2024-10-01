import logging

from odoo import models, fields


_logger = logging.getLogger(__name__)


class HrHospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _inherit = ['human.mixin', ]
    _description = 'Patient'

    birthday = fields.Date()
    age = fields.Integer(
        string="Age",
        compute='_compute_age'
    )

    passport = fields.Text(
        string='Passport'
    )

    contact = fields.Char(
        string='Contact'
    )

    hr_hospital_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string="Doctor",
    )

    def _compute_age(self):
        for record in self:
            if record.birthday:
                record.age = fields.Date.today().year - record.birthday.year
            else:
                record.age = 0
