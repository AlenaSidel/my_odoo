# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LeadLogg(models.Model):
    _inherit = "crm.lead"

    @api.multi
    def write(self, vals):
        if vals.get('email_from'):
            self.message_post("Mail change! New mail: %s" % vals.get('email_from'))

        return super(LeadLogg, self).write(vals)
