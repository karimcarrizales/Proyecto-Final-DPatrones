"""
Archivo    : adapter.py
Descripción: Adaptador entre el sistema nuevo y el inventario legado.
Patrón GoF : Adapter (Estructural)
Curso      : Diseño de Patrones (UCA-IEP026)
"""


from .inventario_legado import InventarioLegado


class InventarioAdapter:

    def __init__(self):
        self.inventario_legado = InventarioLegado()

    def consultar_stock(self, producto):
        resultado = self.inventario_legado.consultar_stock_antiguo(producto)

        return resultado["stock"]