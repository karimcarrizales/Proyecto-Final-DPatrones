"""
Archivo    : inventario_legado.py
Descripción: Sistema antiguo de inventario.
Patrón GoF : Adapter (Estructural)
Curso      : Diseño de Patrones (UCA-IEP026)
"""


class InventarioLegado:

    def consultar_stock_antiguo(self, codigo_producto):
        return {
            "codigo": codigo_producto,
            "stock": 50
        }