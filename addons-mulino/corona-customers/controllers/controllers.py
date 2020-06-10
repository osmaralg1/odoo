# -*- coding: utf-8 -*-
from odoo import http


class Corona-customers(http.Controller):
    @http.route('/corona-customers/corona-customers/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/corona-customers/corona-customers/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('corona-customers.list', {
            'root': '/corona-customers/corona-customers',
            'objects': http.request.env['corona-customers.corona-customers'].search([]),
        })

    @http.route('/corona-customers/corona-customers/objects/<model("corona-customers.corona-customers"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('corona-customers.object', {
            'object': obj
        })
