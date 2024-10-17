import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_ods_author = fields.Boolean()
    ods_book_ids = fields.Boolean()
    ods_books_count = fields.Boolean()
