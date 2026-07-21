"""
Archivo    : pago.py
Descripción: Clases base para el sistema de pagos.
Patrón GoF : Factory Method (Creacional)
Curso      : Diseño de Patrones (UCA-IEP026)
"""


from abc import ABC, abstractmethod


class Pago(ABC):

    @abstractmethod
    def procesar(self, monto):
        pass


class PagoTarjeta(Pago):

    def procesar(self, monto):
        return f"Pago con tarjeta procesado: ${monto}"


class PagoPayPal(Pago):

    def procesar(self, monto):
        return f"Pago con PayPal procesado: ${monto}"