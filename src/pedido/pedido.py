"""
Archivo    : pedido.py
Descripción: Entidad Pedido para el sistema de gestión de pedidos.
Patrón GoF : Builder (Creacional)
Curso      : Diseño de Patrones (UCA-IEP026)
"""


class Pedido:
    def __init__(self):
        self.cliente = None
        self.producto = None
        self.cantidad = 0
        self.direccion = None

    def __str__(self):
        return (
            f"Pedido(cliente={self.cliente}, "
            f"producto={self.producto}, "
            f"cantidad={self.cantidad}, "
            f"direccion={self.direccion})"
        )