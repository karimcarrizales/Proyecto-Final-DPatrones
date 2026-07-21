"""
Archivo    : descuento.py
Descripción: Estrategias de descuento para pedidos.
Patrón GoF : Strategy (Comportamiento)
Curso      : Diseño de Patrones (UCA-IEP026)
"""

from abc import ABC, abstractmethod


class EstrategiaDescuento(ABC):

    @abstractmethod
    def calcular(self, monto):
        pass


class SinDescuento(EstrategiaDescuento):

    def calcular(self, monto):
        return monto


class DescuentoClienteFrecuente(EstrategiaDescuento):

    def calcular(self, monto):
        return monto * 0.90


class DescuentoTemporada(EstrategiaDescuento):

    def calcular(self, monto):
        return monto * 0.80


class CalculadoraDescuento:

    def __init__(self, estrategia):
        self.estrategia = estrategia

    def aplicar(self, monto):
        return self.estrategia.calcular(monto)