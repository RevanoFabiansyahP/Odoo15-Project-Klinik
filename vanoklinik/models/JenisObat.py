from odoo import api, fields, models

class JenisObat(models.Model):
     _name = 'vanoklinik.jenisobat'
     _description = 'New Description'

     name = fields.Selection([
        ('Obat Antibiotik', 'Obat Antibiotik'), 
        ('Obat Cair', 'Obat Cair'), 
        ('Obat Tablet/Kapsul','Obat Tablet/Kapsul'), 
        ('Obat Oles','Obat Oles'),
        ('Obat Tetes','Obat Tetes'),
        ('Alat Medis','Alat Medis')
    ], string='Jenis Obat')
    
     kode_jenis = fields.Char(onchange='_compute_field_name', string='Kode Jenis Obat')
    
     @api.onchange('name')
     def _compute_kode_jenis(self):
        if (self.name=='Obat Antibiotik'):
            self.kode_jenis = 'antibiotik(med-01)'
        elif (self.name == 'Obat Cair'):
            self.kode_jenis = 'obatcair(med-02)'
        elif (self.name == 'Obat Tablet/Kapsul'):
            self.kode_jenis = 'tablet/kapsul(med-03)' 
        elif (self.name == 'Obat Oles'):
            self.kode_jenis = 'obatoles(med-04)' 
        elif (self.name == 'Obat Tetes'):
            self.kode_jenis = 'obattetes(med-05)'
        elif (self.name == 'Alat Medis'):
            self.kode_jenis = 'alatmedis(med-06)'     

    #  kode_kelompok = fields.Char(string='Kode Kelompok')
     kode_lemari = fields.Char(string='Kode Lemari')
     obat_ids = fields.One2many(comodel_name='vanoklinik.obat', 
                                  inverse_name='jenisobat_id', 
                                  string='Daftar Obat')
     jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
     @api.depends('obat_ids')
     def _compute_jml_item(self):
        for rec in self:
            a = self.env['vanoklinik.obat'].search([('jenisobat_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

     daftar = fields.Char(string='Daftar Isi')