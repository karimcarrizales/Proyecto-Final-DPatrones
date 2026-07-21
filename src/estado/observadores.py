"""
Archivo    : observadores.py
Descripción: Observadores concretos para el patrón Observer.
Patrón GoF : Observer (Comportamiento)
Curso      : Diseño de Patrones (UCA-IEP026)
"""

from .pedido_observer import Observador


class ObservadorCliente(Observador):

    def __init__(self):
        self.ultimo_estado = None

    def actualizar(self, estado):
        self.ultimo_estado = estado


class ObservadorLog(Observador):

    def __init__(self):
        self.ultimo_estado = None

    def actualizar(self, estado):
        self.ultimo_estado = estado