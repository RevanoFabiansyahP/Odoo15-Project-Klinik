# -*- coding: utf-8 -*-
{
    'name': "Vano Klinik",

    'summary': """
        Klinik Vanhealty""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',
    'application': True,


    # any module necessary for this one to work correctly
    'depends': ['base','report_xlsx',],

    # only loaded in demonstration mode
    'data': [
        'security/ir.model.access.csv',
        'report/report.xml',
        'report/daftarpenjualan_pdf.xml',
        'report/tebusanresepobat_pdf.xml',
        'views/menu.xml',
        'views/pemilik_view.xml',
        'views/investor_view.xml',
        'views/obat_view.xml',
        'views/jenisobat_view.xml',
        'views/layananklinik_view.xml',
        'views/pegawai_view.xml',
        'views/dokter_view.xml',
        'views/perawat_view.xml',
        'views/petugasapotek_view.xml',
        'views/petugaskebersihan_view.xml',
        'views/mitraklinik_view.xml',
        'views/rujukan_view.xml',
        'views/pasien_view.xml',
        'views/rekammedis_view.xml',
        'views/apotek_view.xml',
        'views/resepobat_view.xml',
        'wizzard/inputobat_wizard_view.xml',


    ],
}