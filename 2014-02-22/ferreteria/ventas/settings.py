from django.conf import settings
from ventas import constants

PREFIJO_BOLETA = getattr(
    settings,
    'PREFIJO_BOLETA',
    constants.PREFIJO_BOLETA
)

PREFIJO_FACTURA = getattr(
    settings,
    'PREFIJO_FACTURA',
    constants.PREFIJO_FACTURA
)
