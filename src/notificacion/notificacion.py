"""
Archivo    : notificacion.py
Descripción: Abstracción para el patrón Bridge de notificaciones.
Patrón GoF : Bridge (Estructural)
Curso      : Diseño de Patrones (UCA-IEP026)
"""

from abc import ABC, abstractmethod


class CanalNotificacion(ABC):

    @abstractmethod
    def enviar(self, mensaje):
        pass


class Notificacion:

    def __init__(self, canal):
        self.canal = canal

    def enviar_mensaje(self, mensaje):
        return self.canal.enviar(mensaje)