import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class HumanMixin(models.AbstractModel):
    _name = 'human.mixin'
    _description = 'Human Mixin'

    first_name = fields.Char()
    last_name = fields.Char()
    phone = fields.Char(String='Phone Number')
    gender = fields.Selection(
        selection=[
            ('male','Male'),
            ('female','Female'),
        ],
    string='Gender'
    )
    foto = fields.Image(
        max_width=512,
        max_height=512,
    )


