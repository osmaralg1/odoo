# -*- coding: utf-8 -*-
from odoo import http


class Corona(http.Controller):
    @http.route('/corona/corona/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/corona/corona/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('corona.list', {
            'root': '/corona/corona',
            'objects': http.request.env['corona.corona'].search([]),
        })

    @http.route('/corona/corona/objects/<model("corona.corona"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('corona.object', {
            'object': obj
        })
