from odoo import api, fields, models

class RekamMedis(models.Model):
    _name = 'vanoklinik.rekammedis'
    _description = 'New Description' 

    name = fields.Many2one(comodel_name='vanoklinik.pasien',
                                         string='Nama Pasien')
    umur = fields.Char(string='Umur')
    j_kelamin = fields.Selection([
        ('Laki-laki','Laki-laki'),('Perempuan','Perempuan')], string='Jenis Kelamin')
    tinggi = fields.Char(string='Tinggi Badan')
    berat = fields.Char(string='Berat Badan')
    keluhan = fields.Selection([
        ('Asma','Asma'),
        ('TBC','TBC'),
        ('Maag','Maag'),
        ('Epilepsi','Epilepsi'),
        ('Varises','Varises'),
        ('Alergi','Alergi'),
        ('Bronchitis','Bronchitis'),
        ('Radang Paru','Radang Paru'),
        ('Sakit Kepala','Sakit Kepala'),
        ('Darah Tinggi','Darah Tinggi'),
        ('Penyakit Jantung','Penyakit Jantung'),
        ('Pingsan Berulang-ulang','Pingsan Berulang-ulang'),
        ('Flu dan Sakit Tenggorokan','Flu dan Sakit Tenggorokan')
        ], string='Keluhan & Riwayat Penyakit')
    no_antrian = fields.Char(string='No Antrian')

    dokter_id = fields.Many2one(comodel_name='vanoklinik.dokter',
                                         string='Dokter',
                                         ondelete='cascade')
    
    pasien_id = fields.Many2one(comodel_name='vanoklinik.rujukan',
                                         string='Rujukan Dari',
                                         ondelete='cascade')
    
    
    @api.onchange('name')
    def onchange_name(self):
        if (self.name):
            self.umur = self.name.umur
            self.j_kelamin = self.name.j_kelamin
            self.tinggi = self.name.tinggi
            self.berat = self.name.berat
            self.no_antrian = self.name.no_antrian

    # @api.model
    # def create (self,vals):
    #     res = super(RekamMedis, self).create(vals)
    #     if (self.name):
    #         self.umur = self.name.umur
    #         self.j_kelamin = self.name.j_kelamin
    #         self.tinggi = self.name.tinggi
    #         self.berat = self.name.berat
    #         self.tgl_lahir = self.name.tgl_lahir
    #         self.alamat = self.name.alamat
    #     return res