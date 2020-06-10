# -*- coding: utf-8 -*-

from odoo import models, fields, api


class corona(models.Model):
    _name = 'corona.corona'
    _description = 'corona.corona'

    name = fields.Char(size=100)
    email = fields.Char(size=100)
    telephone = fields.Char(size=50)
    timeFrom = fields.Datetime()
    timeTo = fields.Datetime()
