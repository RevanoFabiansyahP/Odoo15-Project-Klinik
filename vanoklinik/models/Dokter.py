from odoo import api, fields, models

class Dokter(models.Model):
    _name = 'vanoklinik.dokter'
    _description = 'New Description' 

    name = fields.Char(string='Nama')
    spesialis = fields.Selection([
        ('Dokter Anak','Dokter Anak'),
        ('Dokter Umum','Dokter Umum'),
        ('Dokter THT','Dokter THT'),
        ('Dokter Mata','Dokter Mata'),
        ('Dokter Gigi','Dokter Gigi'),
        ('Dokter Kulit','Dokter Kulit')
        ], string='Spesialis')
    alamat = fields.Char(string='Alamat')
    j_kelamin = fields.Selection([
        ('Laki-laki','Laki-laki'),('Perempuan','Perempuan')], string='Jenis Kelamin')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    
    id_dokter = fields.Char(string='ID Dokter')

    pictures = fields.Image(string="Gambar")