"""
Archivo    : factory.py
Descripción: Fábrica para crear objetos de pago.
Patrón GoF : Factory Method (Creacional)
Curso      : Diseño de Patrones (UCA-IEP026)
"""


from .pago import PagoTarjeta, PagoPayPal


class PagoFactory:

    @staticmethod
    def crear_pago(tipo):
        if tipo.lower() == "tarjeta":
            return PagoTarjeta()

        elif tipo.lower() == "paypal":
            return PagoPayPal()

        else:
            raise ValueError("Tipo de pago no soportado")