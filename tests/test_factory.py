"""
Pruebas del patrón Factory Method para pagos.
"""

from src.pago.factory import PagoFactory


def test_factory_crea_pago_tarjeta():
    pago = PagoFactory.crear_pago("tarjeta")

    resultado = pago.procesar(100)

    assert "tarjeta" in resultado.lower()
    assert "100" in resultado


def test_factory_crea_pago_paypal():
    pago = PagoFactory.crear_pago("paypal")

    resultado = pago.procesar(200)

    assert "paypal" in resultado.lower()
    assert "200" in resultado


def test_factory_rechaza_pago_no_soportado():
    try:
        PagoFactory.crear_pago("bitcoin")
        assert False
    except ValueError:
        assert True