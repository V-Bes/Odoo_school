import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class HrHospitalDisease(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Disease'
    _parent_store = True  # Включает поддержку хранения иерархии
    _parent_name = 'parent_id'  # Указывает поле родительской связи
    _rec_name = 'name'

    name = fields.Char(
        string='Disease',
        required=True)

    parent_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string='Parent Disease',
        index=True,
        ondelete='restrict'
    )

    child_ids = fields.One2many(
        comodel_name='hr.hospital.disease',
        inverse_name='parent_id',
        string='Child Disease'
    )

    parent_path = fields.Char(
        index=True
    )

    display_name = fields.Char(
        compute='_compute_display_name',
        store=True
    )

    is_category = fields.Boolean()

    @api.depends('name', 'parent_id')
    def _compute_display_name(self):
        for disease in self:
            if disease.parent_id:
                disease.display_name = '%s / %s' % (
                    disease.parent_id.display_name, disease.name)
            else:
                disease.display_name = disease.name
