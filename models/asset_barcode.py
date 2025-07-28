from odoo import models, fields

class AssetBarcode(models.Model):
    _name = 'asset.barcode'
    _description = 'Asset Barcode'

    name = fields.Char(string='Asset Name', required=True)
    barcode = fields.Char(string='Barcode')
