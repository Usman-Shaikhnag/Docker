from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool, PoolMeta

__all__ = ['QualityControlProduction','QualityShipmentIn','ProdShipment']

class QualityControlProduction(ModelSQL, ModelView):
    "Quality Control Production"
    __name__ = 'production'
    
    inwardno = fields.Many2Many('prod.shipment.relation',
        'prodid','shipid', 'Inward',domain=[
            ('state', '=', 'done'),
            ])

   

class QualityShipmentIn(ModelSQL,ModelView):
    "Quality Shipment In"
    __name__ = "stock.shipment.in"
    inwardid = fields.Many2One('production','Inward ID')
    prodstate = fields.Boolean("In Production")

class ProdShipment(ModelSQL):
    
    "Prod Shipment Relation"
    __name__ = "prod.shipment.relation"
    
    shipid = fields.Many2One('stock.shipment.in','Shipment ID')
    prodid = fields.Many2One('production','Production ID')