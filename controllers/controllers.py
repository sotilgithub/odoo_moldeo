# -*- coding: utf-8 -*-
# from odoo import http


# class BasicoGenerado4(http.Controller):
#     @http.route('/basico_generado4/basico_generado4/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/basico_generado4/basico_generado4/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('basico_generado4.listing', {
#             'root': '/basico_generado4/basico_generado4',
#             'objects': http.request.env['basico_generado4.basico_generado4'].search([]),
#         })

#     @http.route('/basico_generado4/basico_generado4/objects/<model("basico_generado4.basico_generado4"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('basico_generado4.object', {
#             'object': obj
#         })
