import logging
from odoo import models, fields, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HrHospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _inherit = ['human.mixin']
    _description = 'Doctor'
    _rec_name = 'last_name'

    description = fields.Text()

    is_intern = fields.Boolean(
        string="Intern",
        default=False
    )

    mentor = fields.Many2one(
        comodel_name="hr.hospital.doctor",
        domain=[
            ('is_intern','=',False)
        ],
    )

    active = fields.Boolean(
        default=True,
    )

    specialization = fields.Selection(selection=[
        ('family_doctor', 'Family doctor'),
        ('obstetrician', 'Obstetrician'),
        ('pharmacist', 'Pharmacist'),
        ('neurologist', 'Neurologist'),
    ])

    @api.constrains('mentor')
    def _check_duplicate(self):
        for record in self:
            if record.id == record.mentor.id:
                raise ValidationError(
                    'A doctor cannot be his own mentor.')
            if not record.is_intern:
                raise ValidationError(
                    'Choosing a mentor is only possible for an intern.')
