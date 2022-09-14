from turtle import width
from odoo import models, fields

class ReportObat(models.AbstractModel):
    _name = 'report.vanoklinik.report_obat_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()
    
    def generate_xlsx_report(self, workbook, data, obat):
        sheet = workbook.add_worksheet('Daftar obat')
        bold = workbook.add_format({'bold': True})
        
        sheet.write(0, 0, 'Tanggal Laporan :', bold)
        sheet.write(0, 1, str(self.tgl_lap))
        sheet.write(2, 0, 'Nama Obat', bold)
        sheet.write(2, 1, 'Harga Modal', bold)
        sheet.write(2, 2, 'Harga Jual', bold)
        sheet.write(2, 3, 'Stok', bold)
        sheet.write(2, 4, 'Jenis Obat', bold)
        sheet.write(2, 5, 'Supplier Penerima', bold)

        row = 3
        col = 0
        for obj in obat:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.harga_supplier)
            sheet.write(row, col+2, obj.harga_jual)
            sheet.write(row, col+3, obj.stok)
            for xxx in obj.jenisobat_id:
                sheet.write(row, col +4, xxx.name)
            for xxx in obj.mitraklinik_id:
                sheet.write(row, col +5, xxx.name)
                row += 1
            row += 1