from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit='res.partner'
    _description = 'New Description'

    is_pemilik = fields.Boolean(string='Is Pemilik')
    is_investor = fields.Boolean(string='Is Investor')