"""
Pruebas del patrón Abstract Factory para pagos.
"""

from src.pago.abstract_factory import (
    FabricaPagoProduccion,
    FabricaPagoPruebas
)


def test_fabrica_produccion_crea_pagos():
    fabrica = FabricaPagoProduccion()

    tarjeta = fabrica.crear_tarjeta()
    paypal = fabrica.crear_paypal()

    assert tarjeta.__class__.__name__ == "PagoTarjeta"
    assert paypal.__class__.__name__ == "PagoPayPal"


def test_fabrica_pruebas_crea_pagos():
    fabrica = FabricaPagoPruebas()

    tarjeta = fabrica.crear_tarjeta()
    paypal = fabrica.crear_paypal()

    assert tarjeta.__class__.__name__ == "PagoTarjeta"
    assert paypal.__class__.__name__ == "PagoPayPal"