"""
Archivo    : abstract_factory.py
Descripción: Fábrica abstracta para crear familias de pagos.
Patrón GoF : Abstract Factory (Creacional)
Curso      : Diseño de Patrones (UCA-IEP026)
"""

from abc import ABC, abstractmethod

from .pago import PagoTarjeta, PagoPayPal


class FabricaPago(ABC):

    @abstractmethod
    def crear_tarjeta(self):
        pass

    @abstractmethod
    def crear_paypal(self):
        pass


class FabricaPagoProduccion(FabricaPago):

    def crear_tarjeta(self):
        return PagoTarjeta()

    def crear_paypal(self):
        return PagoPayPal()


class FabricaPagoPruebas(FabricaPago):

    def crear_tarjeta(self):
        return PagoTarjeta()

    def crear_paypal(self):
        return PagoPayPal()