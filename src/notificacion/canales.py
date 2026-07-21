"""
Archivo    : canales.py
Descripción: Implementaciones concretas de canales de notificación.
Patrón GoF : Bridge (Estructural)
Curso      : Diseño de Patrones (UCA-IEP026)
"""


from .notificacion import CanalNotificacion


class CanalEmail(CanalNotificacion):

    def enviar(self, mensaje):
        return f"Email enviado: {mensaje}"


class CanalSMS(CanalNotificacion):

    def enviar(self, mensaje):
        return f"SMS enviado: {mensaje}"