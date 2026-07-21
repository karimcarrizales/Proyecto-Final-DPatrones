"""
Archivo    : pedido_observer.py
Descripción: Implementación del patrón Observer para cambios de estado.
Patrón GoF : Observer (Comportamiento)
Curso      : Diseño de Patrones (UCA-IEP026)
"""


from abc import ABC, abstractmethod


class Observador(ABC):

    @abstractmethod
    def actualizar(self, estado):
        pass


class PedidoEstado:

    def __init__(self):
        self.observadores = []
        self.estado = None

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

        for observador in self.observadores:
            observador.actualizar(nuevo_estado)