from odoo import api, fields, models


class Pegawai(models.Model):
    _name = 'vanoklinik.pegawai'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    j_kelamin = fields.Selection([
        ('Laki-laki','Laki-laki'),('Perempuan','Perempuan')], string='Jenis Kelamin')
    tgl_lahir = fields.Date(string='Tanggal Lahir')

class Perawat(models.Model):
    _name = 'vanoklinik.perawat'
    _inherit = 'vanoklinik.pegawai'
    _description = 'New Description'

    id_perawat = fields.Char(string='ID Perawat')

class PetugasApotek(models.Model):
    _name = 'vanoklinik.petugasapotek'
    _inherit = 'vanoklinik.pegawai'
    _description = 'New Description'

    id_petugasapotek = fields.Char(string='ID Petugas Apotek')

class PetugasKebersihan(models.Model):
    _name = 'vanoklinik.petugaskebersihan'
    _inherit = 'vanoklinik.pegawai'
    _description = 'New Description'

    id_petugaskebersihan = fields.Char(string='ID Petugas Kebersihan')
