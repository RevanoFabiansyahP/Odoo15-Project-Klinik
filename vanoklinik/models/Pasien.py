from odoo import api, fields, models

class Pasien(models.Model):
    _name = 'vanoklinik.pasien'
    _description = 'New Description' 

    name = fields.Char(string='Nama')
    umur = fields.Char(string='Umur')
    j_kelamin = fields.Selection([
        ('Laki-laki','Laki-laki'),('Perempuan','Perempuan')], string='Jenis Kelamin')
    tinggi = fields.Char(string='Tinggi Badan')
    berat = fields.Char(string='Berat Badan')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    alamat = fields.Char(string='Alamat')
    # keluhan = fields.Selection([
    #     ('asma','Asma'),
    #     ('tbc','TBC'),
    #     ('maag','Maag'),
    #     ('epilepsi','Epilepsi'),
    #     ('varises','Varises'),
    #     ('alergi','Alergi'),
    #     ('bronchitis','Bronchitis'),
    #     ('radang paru','Radang Paru'),
    #     ('sakit kepala','Sakit Kepala'),
    #     ('darah tinggi','Darah Tinggi'),
    #     ('penyakit jantung','Penyakit Jantung'),
    #     ('pingsan berulang','Pingsan Berulang-ulang'),
    #     ('flu sakit tenggorokan','Flu dan Sakit Tenggorokan')
    #     ], string='Keluhan')
    
    no_antrian = fields.Char(string='No Antrian')