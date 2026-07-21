"""
Pruebas del patrón Bridge para notificaciones.
"""

from src.notificacion.notificacion import Notificacion
from src.notificacion.canales import CanalEmail, CanalSMS


def test_notificacion_con_email():

    notificacion = Notificacion(CanalEmail())

    resultado = notificacion.enviar_mensaje("Pedido enviado")

    assert resultado == "Email enviado: Pedido enviado"


def test_notificacion_con_sms():

    notificacion = Notificacion(CanalSMS())

    resultado = notificacion.enviar_mensaje("Pedido enviado")

    assert resultado == "SMS enviado: Pedido enviado"