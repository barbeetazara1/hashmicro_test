# -*- coding: utf-8 -*-
from odoo import http

# class BookingOrderBaronBetazara17012025(http.Controller):
#     @http.route('/booking_order__baron__betazara_17012025/booking_order__baron__betazara_17012025/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order__baron__betazara_17012025/booking_order__baron__betazara_17012025/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order__baron__betazara_17012025.listing', {
#             'root': '/booking_order__baron__betazara_17012025/booking_order__baron__betazara_17012025',
#             'objects': http.request.env['booking_order__baron__betazara_17012025.booking_order__baron__betazara_17012025'].search([]),
#         })

#     @http.route('/booking_order__baron__betazara_17012025/booking_order__baron__betazara_17012025/objects/<model("booking_order__baron__betazara_17012025.booking_order__baron__betazara_17012025"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order__baron__betazara_17012025.object', {
#             'object': obj
#         })