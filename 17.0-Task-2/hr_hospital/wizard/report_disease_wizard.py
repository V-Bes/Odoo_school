from odoo import models, fields
from odoo.fields import Datetime


class ReportDiseaseWizard(models.TransientModel):
    _name = 'report.disease.wizard'
    _description = 'Report Wizard'

    doctor_ids = fields.Many2many(
        comodel_name='hr.hospital.doctor',
        )

    disease_ids = fields.Many2many(
        comodel_name='hr.hospital.disease',
        )

    date_from = fields.Date(
        required=True,
        default=Datetime.today()
    )

    date_to = fields.Date(
        required=True,
        default=Datetime.today()
    )

    def report_disease_wizard(self):
        domain_diagnosis = []
        if self.date_from:
            domain_diagnosis.append(('hr_hospital_visit_id.visit_date', '>=',
                                     self.date_from))
        if self.date_to:
            domain_diagnosis.append(('hr_hospital_visit_id.visit_date', '<=',
                                     self.date_to))
        if self.disease_ids:
            domain_diagnosis.append(('hr_hospital_disease_id', 'in',
                                     self.disease_ids.ids))
        if self.doctor_ids:
            domain_diagnosis.append(('hr_hospital_visit_id'
                                     '.hr_hospital_doctor_id', 'in',
                                     self.doctor_ids.ids)
                                    )

        diagnosis_records = (self.env['hr.hospital.diagnosis']
                             .search(domain_diagnosis, order='name'))

        if not diagnosis_records:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'No records found',
                    'message': 'No diagnosis records match your criteria.',
                    'sticky': False,
                }
            }

        return self.env.ref(
            'hr_hospital.hr_hospital_disease_main_report').report_action(
            diagnosis_records)
