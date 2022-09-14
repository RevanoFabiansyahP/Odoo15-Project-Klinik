from odoo import http, models, fields
from odoo.http import request
import json

class Vanoklinik(http.Controller):
    @http.route('/vanoklinik/getobat', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['vanoklinik.obat'].search([])
        isi = []
        for bb in barang:
            isi.append({
                'nama_obat' :bb.name,
                'harga_jual' : bb.harga_jual,
                'stok': bb.stok
            })
        return json.dumps(isi)

class Vanoklinik(http.Controller):
    @http.route('/vanoklinik/getmitra', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['vanoklinik.mitraklinik'].search([])
        mit = []
        for s in supplier:
            mit.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telpon' : s.no_telp,
                'nama_obat' : s.obat_id[0].name
            })
        return json.dumps(mit)
