from email.policy import default
from logging import exception
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResepObat(models.Model):
    _name = 'vanoklinik.resepobat'
    _description = 'New Description'

    name = fields.Many2one(comodel_name='vanoklinik.rekammedis',
                                         string='Nama Pasien')

    no_antrian = fields.Char(string='No Antrian')

    umur = fields.Char(string='Umur')
    j_kelamin = fields.Char(string='Jenis Kelamin')

    keluhan = fields.Char(string='Keluhan')

    dokter_id = fields.Many2one(comodel_name='vanoklinik.dokter',
                                         string='Dokter Yang Menangani',
                                         ondelete='cascade')
    
    pasien_id = fields.Many2one(comodel_name='vanoklinik.rujukan',
                                         string='Rujukan Dari',
                                         ondelete='cascade')
    
    petugasapotek_id = fields.Many2one(comodel_name='vanoklinik.petugasapotek',
                                         string='Petugas Apotek',
                                         ondelete='cascade')

    tgl_penjualan = fields.Datetime(string='Tanggal Transaksi', 
                                    default = fields.Datetime.now())
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    tebusobat_ids = fields.One2many(comodel_name='vanoklinik.tebusobat', 
                                          inverse_name='tebusobat_id', 
                                          string='Detail Tebus Resep Obat')
    state = fields.Selection(
        string='Status',
        selection=[('draft','Draft'),('confirm','Confirm'),('done','Done'),('cancelled','Cancel')],
        required=True, readonly=True, default='draft')
    
    def action_confirm(self):
        self.write({'state': 'confirm'})
    
    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})
    
    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('tebusobat_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['vanoklinik.tebusobat'].search([('tebusobat_id', '=', rec.id)]).mapped('subtotal'))
            rec.total_bayar = a

    @api.ondelete(at_uninstall=False)
    def _ondelete_tebusobat(self):
        if self.tebusobat_ids:
            a=[]
            for rec in self:
                a = self.env['vanoklinik.tebusobat'].search([('tebusobat_id','=',rec.id)])
                print(a)
            for ob in a:
                print(str(ob.obat_id.name) + ' ' + str(ob.qty))
                ob.obat_id.stok += ob.qty
        

    # Untuk Odoo 14
    # def unlink(self):
    #     if self. filtered(lambda line: line.state != "draft"):
    #        raise ValidationError("Tidak dapat menghapus jika status Bukan Draft")
    #     else:
    #     if self.detailpenjualan_ids:
    #         a=[]
    #         for rec in self:
    #             a = self.env['vanomart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
    #             print(a)
    #         for ob in a:
    #             print(str(ob.barang_id.name) + ' ' + str(ob.qty))
    #             ob.barang_id.stok += ob.qty
    #     record = super (Penjualan,self).unlink()
    
    def write (self,vals):
        for rec in self:
            a = self.env['vanoklinik.tebusobat'].search([('tebusobat_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.obat_id.name)+' '+str(data.qty)+' '+str(data.obat_id.stok))
                data.obat_id.stok += data.qty
        record = super (ResepObat,self).write(vals)
        for rec in self:
            b = self.env['vanoklinik.tebusobat'].search([('tebusobat_id','=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.obat_id.name)+' '+str(databaru.qty)+' '+str(databaru.obat_id.stok))
                    databaru.obat_id.stok -= databaru.qty
                else:
                    pass
        return record

    # _sql_constraints = [
    #     ('no_antrian_unik','unique (name)','Nomor Antrian Tidak Boleh Sama !')
    # ]

    @api.onchange('name')
    def onchange_name(self):
        if (self.name):
            self.umur = self.name.umur
            self.j_kelamin = self.name.j_kelamin
            self.keluhan = self.name.keluhan
            self.no_antrian = self.name.no_antrian
            self.dokter_id = self.name.dokter_id
            self.pasien_id = self.name.pasien_id
    
class TebusObat(models.Model):
    _name = 'vanoklinik.tebusobat'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    tebusobat_id = fields.Many2one(comodel_name='vanoklinik.resepobat', 
                                   string='Detail Resep Obat',)
    obat_id = fields.Many2one(comodel_name='vanoklinik.obat', 
                                   string='List Obat')
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')
    
    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan
    
    @api.onchange('obat_id')
    def onchange_obat_id(self):
        if (self.obat_id.harga_jual):
            self.harga_satuan = self.obat_id.harga_jual

    @api.model
    def create(self, vals):
        record = super(TebusObat,self).create(vals)
        if record.qty:
            self.env['vanoklinik.obat'].search([('id','=', record.obat_id.id)]).write({'stok': record.obat_id.stok - record.qty})
        return record

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Mau beli {} Berapa Banyak Sih Ka :)".format(rec.obat_id.name))
            elif (rec.obat_id.stok < rec.qty):
                raise ValidationError("Maaf Stok {} tidak mencukupi, hanya tersedia {}".format(rec.obat_id.name,rec.obat_id.stok))
            
 