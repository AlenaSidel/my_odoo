# -*- coding: utf-8 -*-
from odoo import http

# class MyCrm(http.Controller):
#     @http.route('/my_crm/my_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_crm/my_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_crm.listing', {
#             'root': '/my_crm/my_crm',
#             'objects': http.request.env['my_crm.my_crm'].search([]),
#         })

#     @http.route('/my_crm/my_crm/objects/<model("my_crm.my_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_crm.object', {
#             'object': obj
#         })
