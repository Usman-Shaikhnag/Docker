# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
# from qualitycontrol import QualityControl
from . import qualitycontrol
from . import production
__all__ = ['register']


def register():
    Pool.register(
        qualitycontrol.PreProductionLabCritarea,
        qualitycontrol.QualityControlPreproduction,
        qualitycontrol.QualityControlPostproduction,
        production.QualityControlProduction,
        production.QualityShipmentIn,
        module='quality_control', type_='model')
    Pool.register(
        module='quality_control', type_='wizard')
    Pool.register(
        module='quality_control', type_='report')
