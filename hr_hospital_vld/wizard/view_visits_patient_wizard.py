import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class ViewVisitsPatientWizard(models.TransientModel):
    _name = 'view.visits.patient.wizard'
    _description = 'View visits'

    visits_id = fields.Many2many(
        comodel_name='hr.hospital.visit',
        readonly=True,
    )

    @api.model
    def default_get(self, fields_list):
        res = super(ViewVisitsPatientWizard, self).default_get(fields_list)
        patient_id = self.env.context.get('active_id')
        if patient_id:
            visits = self.env['hr.hospital.visit'].search(
                [('hr_hospital_patient_id', '=', patient_id)])
            res['visits_id'] = [(6, 0, visits.ids)]
        return res
