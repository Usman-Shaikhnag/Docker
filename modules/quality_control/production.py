from trytond.model import ModelSQL, ModelView, fields

__all__ = ['QualityControlProduction','QualityShipmentIn']

class QualityControlProduction(ModelSQL, ModelView):
    "Quality Control Production"
    __name__ = 'production'
    
    # customername = fields.Many2One('party.party' , 'Party')
    inwardno = fields.One2Many('stock.shipment.in',
        'inwardid', 'Inward No')

class QualityShipmentIn(ModelSQL,ModelView):
    "Quality Shipment In"
    __name__ = "stock.shipment.in"
    inwardid = fields.Many2One('production','Inward ID')
