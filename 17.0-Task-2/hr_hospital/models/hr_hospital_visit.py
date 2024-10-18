import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

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
            ('planned', 'planned'),
            ('completed', 'completed'),
            ('cancel', 'cancel'),
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

    hr_hospital_diagnosis_ids = fields.One2many(
        comodel_name='hr.hospital.diagnosis',
        inverse_name='hr_hospital_visit_id',
        string="Diagnosis",
    )

    start_visit_date = fields.Date(
        default=fields.Date.today(),
        required=True,
    )
    end_visit_date = fields.Date(
        default=fields.Date.today(),
    )

    display_name = fields.Char(
        compute='_compute_display_name',
        store=True
    )

    @api.depends('planned_date', 'visit_date')
    def _compute_display_name(self):
        for diagnosis in self:
            if diagnosis.visit_date:
                diagnosis.display_name = '%s / %s' % (
                    diagnosis.visit_date, diagnosis.planned_date)
            else:
                diagnosis.display_name = diagnosis.planned_date

    @api.constrains('planned_date', 'visit_date',
                    'hr_hospital_doctor_id')
    def _check_planned_date(self):
        for record in self:
            if record.status_visit == 'completed':
                raise ValidationError(_('It is forbidden to change '
                                        '"Planned date" , "Visit date", '
                                        '"Doctor" in the status '
                                        '"completed"'))

    @api.ondelete(at_uninstall=False)
    def _prevent_delete(self):
        for record in self:
            if record.hr_hospital_diagnosis_ids:
                raise ValidationError(_(
                    "You cannot delete a visit that has 'diagnosis'."))

    @api.constrains('hr_hospital_doctor_id', 'hr_hospital_patient_id',
                    'visit_date')
    def _check_duplicate(self):
        for record in self:
            is_duplicate = self.search([
                ('hr_hospital_doctor_id', '=',
                 record.hr_hospital_doctor_id.id),
                ('hr_hospital_patient_id', '=',
                 record.hr_hospital_patient_id.id),
                ('visit_date', '=', record.visit_date),
                ('id', '!=', record.id),
            ])
            if is_duplicate:
                raise ValidationError(_('Duplicate visit found for the same '
                                      'doctor, patient, and date.'))
