from odoo import api, fields, models

class Obat(models.Model):
     _name = 'vanoklinik.obat'
     _description = 'New Description'

     name = fields.Char(string='Nama Obat')
     harga_supplier = fields.Integer(string='Harga Supplier',required=True)
     harga_jual = fields.Integer(string='Harga Jual',required=True)
     
     # Perubahannya ada di sini
     jenisobat_id = fields.Many2one(comodel_name='vanoklinik.jenisobat',
                                         string='Jenis Obat',
                                         ondelete='cascade')
                                        
    # Perubahannya di sini
     mitraklinik_id = fields.Many2many(comodel_name='vanoklinik.mitraklinik', string='Mitra Klinik')
     
    # perubahan stok
     stok = fields.Integer(string='Stok')

    # tambah gambar
     pictures = fields.Image(string="Gambar")

