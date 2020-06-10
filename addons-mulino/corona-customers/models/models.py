# -*- coding: utf-8 -*-

from odoo import models, fields, api


class corona_customers(models.Model):
    _name = 'corona-customers.corona-customers'
    _description = 'corona-customers.corona-customers'

    name = fields.Char(size=100)
    telephone = fields.Char(size=50)
    email = fields.Char(size=100)
    date = fields.Date()
    timeFrom = fields.Date()
    timeTo = fields.Date() 


