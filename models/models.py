# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class LeadLogg(models.Model):
    _name = "crm.lead"
    _inherit = "crm.lead"

    @api.multi
    def write(self, vals):
        #_logger.info("mail change!")
        if vals.get('email_from'):
            self.message_post("Mail change! New mail: %s" % vals.get('email_from'))

        return super(LeadLogg, self).write(vals)
