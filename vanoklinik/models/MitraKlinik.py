from odoo import api, fields, models


class MitraKlinik(models.Model):
    _name = 'vanoklinik.mitraklinik'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    obat_id = fields.Many2many(comodel_name='vanoklinik.obat', string='Obat')

class RujukanRumahSakit(models.Model):
    _name = 'vanoklinik.rujukan'
    _description = 'New Description'

    name = fields.Char(string='Nama Rumah Sakit')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    pasien_id = fields.Many2many(comodel_name='vanoklinik.rekammedis', string='Pasien')