import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    '''
    This model test
    '''
    _inherit = "res.partner"
