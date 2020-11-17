# -*- coding: utf-8 -*-
# from odoo import http


# class MfPaid(http.Controller):
#     @http.route('/mf_paid/mf_paid/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mf_paid/mf_paid/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mf_paid.listing', {
#             'root': '/mf_paid/mf_paid',
#             'objects': http.request.env['mf_paid.mf_paid'].search([]),
#         })

#     @http.route('/mf_paid/mf_paid/objects/<model("mf_paid.mf_paid"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mf_paid.object', {
#             'object': obj
#         })
