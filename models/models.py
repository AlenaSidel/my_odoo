# -*- coding: utf-8 -*-

from odoo import models, fields


class LeadLogg(models.Model):
    _inherit = "crm.lead"

    email_from = fields.Char(track_visibility='onchange')
