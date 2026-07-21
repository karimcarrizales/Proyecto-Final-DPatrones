"""
Pruebas del patrón Adapter para inventario.
"""

from src.inventario.adapter import InventarioAdapter


def test_adapter_consulta_stock():

    inventario = InventarioAdapter()

    stock = inventario.consultar_stock("A001")

    assert stock == 50