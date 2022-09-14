from odoo import api, fields, models

class LayananKlinik(models.Model):
     _name = 'vanoklinik.layanan'
     _description = 'New Description'

     name = fields.Char(string='Nama Layanan')
     harga_jasa = fields.Integer(string='Harga Jasa',required=True)
                                        

