import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HrGroupChangePatient(models.TransientModel):
    _name = 'hr.group.change.patient.wizard'
    _description = 'Group change patient.'

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        readonly=True,
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
    )

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        active_ids = self.env.context.get('active_id')
        #print(self.env.context)
        #for record in active_ids:
        #   patient_id = self.env['hr.hospital.patient'].browse(self.env.context.get('active_id'))
        #    res['patient_id'] = patient_id.id
        #     res['res_partner_ids'] = [
        #         (6, 0, book_id.res_partner_readers_ids.ids)]
        return res

    def change_patient(self):
        active_ids = self.env.context.get('active_ids')
        for record in active_ids:
            patient_id = self.env['hr.hospital.patient'].browse(record)
            patient_id.hr_hospital_doctor_id = self.doctor_id
