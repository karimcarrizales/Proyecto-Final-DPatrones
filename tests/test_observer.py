"""
Pruebas del patrón Observer para cambios de estado del pedido.
"""

from src.estado.pedido_observer import PedidoEstado
from src.estado.observadores import ObservadorCliente, ObservadorLog


def test_observer_notifica_a_todos():

    pedido = PedidoEstado()

    cliente = ObservadorCliente()
    log = ObservadorLog()

    pedido.agregar_observador(cliente)
    pedido.agregar_observador(log)

    pedido.cambiar_estado("Enviado")

    assert cliente.ultimo_estado == "Enviado"
    assert log.ultimo_estado == "Enviado"