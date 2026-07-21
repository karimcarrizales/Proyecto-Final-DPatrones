"""
Pruebas del patrón Strategy para descuentos.
"""

from src.descuento.descuento import (
    CalculadoraDescuento,
    SinDescuento,
    DescuentoClienteFrecuente,
    DescuentoTemporada
)


def test_sin_descuento():

    calculadora = CalculadoraDescuento(SinDescuento())

    resultado = calculadora.aplicar(100)

    assert resultado == 100


def test_descuento_cliente_frecuente():

    calculadora = CalculadoraDescuento(DescuentoClienteFrecuente())

    resultado = calculadora.aplicar(100)

    assert resultado == 90


def test_descuento_temporada():

    calculadora = CalculadoraDescuento(DescuentoTemporada())

    resultado = calculadora.aplicar(100)

    assert resultado == 80