import logging

from odoo import models, fields, api, _
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

    hr_hospital_patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string="Patient",
    )

    hr_hospital_disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string="Disease",
    )

    visit_planned_date = fields.Datetime(
        compute='_compute_planned_date',
        store=True,
    )

    disease_parent_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        compute='_compute_disease_parent',
        store=True,
    )

    display_name = fields.Char(
        compute='_compute_display_name',
        store=True
    )

    @api.depends('hr_hospital_disease_id.name')
    def _compute_display_name(self):
        for diagnosis in self:
            if diagnosis.hr_hospital_disease_id:
                diagnosis.name = diagnosis.hr_hospital_disease_id.name

    @api.onchange('approved')
    def _onchange_approved(self):
        if (self.approved
                and self.hr_hospital_visit_id.hr_hospital_doctor_id.is_intern):
            raise ValidationError(_('The intern cannot '
                                    'confirm the diagnosis.'))

    @api.depends('hr_hospital_visit_id.planned_date')
    def _compute_planned_date(self):
        for diagnosis in self:
            if diagnosis.hr_hospital_visit_id:
                diagnosis.visit_planned_date = (diagnosis.hr_hospital_visit_id
                                                .planned_date)

    @api.depends('hr_hospital_disease_id.parent_id')
    def _compute_disease_parent(self):
        for diagnosis in self:
            if diagnosis.hr_hospital_disease_id:
                diagnosis.disease_parent_id = (diagnosis
                                               .hr_hospital_disease_id
                                               .parent_id
                                               )
