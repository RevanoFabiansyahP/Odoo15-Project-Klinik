from odoo import api, fields, models

class InputObat(models.TransientModel):
    _name = 'vanoklinik.inputobat'
     
    
    obat_id = fields.Many2one(
        comodel_name='vanoklinik.obat',
        string='Nama Obat',
        required=True)

    jumlah = fields.Integer(
        string='Jumlah',
        required=False)

    def button_input_obat(self):
        for rec in self:
            self.env['vanoklinik.obat'].search([('id', '=', rec.obat_id.id)]).write({'stok':rec.obat_id.stok + rec.jumlah})