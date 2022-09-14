from odoo import api, fields, models

class PemilikKlinik(models.Model):
    _inherit = 'res.partner'
    _description = 'pemilik'

    poin = fields.Integer(string='Poin')
    level = fields.Integer(string='Level')
    