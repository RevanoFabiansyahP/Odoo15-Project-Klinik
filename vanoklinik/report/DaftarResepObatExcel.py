from datetime import timedelta
from odoo import models, fields

class ReportResepObat(models.AbstractModel):
    _name = 'report.vanoklinik.report_resepobat_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()
    
    def generate_xlsx_report(self, workbook, data, resepobat):
        sheet = workbook.add_worksheet('Riwayat Resep Obat')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, 'Tanggal Laporan :', bold)
        sheet.write(0, 1, str(self.tgl_lap))
        sheet.write(2, 0, 'No Antrian', bold)
        sheet.write(2, 1, 'Nama Pasien', bold)
        sheet.write(2, 2, 'Umur', bold)
        sheet.write(2, 3, 'Jenis kelamin', bold)
        sheet.write(2, 4, 'Keluhan', bold)
        sheet.write(2, 5, 'Dokter Yang Menangani', bold)
        sheet.write(2, 6, 'Rujukan dari', bold)
        sheet.write(2, 7, 'Petugas Apotek', bold)
        sheet.write(2, 8, 'Tanggal Transaksi', bold)
        sheet.write(2, 9, 'Nama Barang', bold)
        sheet.write(2, 10, 'Harga', bold)
        sheet.write(2, 11, 'Jumlah Beli', bold)
        sheet.write(2, 12, 'Subtotal', bold)
        sheet.write(2, 13, 'Total Pembayaran', bold)

        row = 3
        col = 0
        for obj in resepobat:
            col = 0
            sheet.write(row, col, obj.no_antrian)
            sheet.write(row, col+1, obj.name.name.name)
            sheet.write(row, col+2, obj.umur)
            sheet.write(row, col+3, obj.j_kelamin)
            sheet.write(row, col+4, obj.keluhan)
            sheet.write(row, col+5, obj.dokter_id.name)
            sheet.write(row, col+6, obj.pasien_id.name)
            sheet.write(row, col+7, obj.petugasapotek_id.name)
            sheet.write(row, col+8, (obj.tgl_penjualan+ timedelta(hours=7)).strftime("%d/%m/%Y, %H:%M:%S"))
            sheet.write(row, col+13, obj.total_bayar)
            for xxx in obj.tebusobat_ids:
                sheet.write(row, col +9, xxx.obat_id.name)
                sheet.write(row, col +10, xxx.harga_satuan)
                sheet.write(row, col +11, xxx.qty)
                sheet.write(row, col +12, xxx.subtotal)
                row += 1
            row += 1
