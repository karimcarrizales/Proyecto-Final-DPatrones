"""
Archivo    : builder.py
Descripción: Construcción paso a paso de objetos Pedido.
Patrón GoF : Builder (Creacional)
Curso      : Diseño de Patrones (UCA-IEP026)
"""

from .pedido import Pedido


class PedidoBuilder:
    def __init__(self):
        self.pedido = Pedido()

    def con_cliente(self, cliente):
        self.pedido.cliente = cliente
        return self

    def con_producto(self, producto):
        self.pedido.producto = producto
        return self

    def con_cantidad(self, cantidad):
        self.pedido.cantidad = cantidad
        return self

    def con_direccion(self, direccion):
        self.pedido.direccion = direccion
        return self

    def build(self):
        return self.pedido