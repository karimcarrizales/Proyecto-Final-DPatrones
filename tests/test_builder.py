from src.pedido.builder import PedidoBuilder


def test_builder_crea_pedido_completo():
    pedido = (
        PedidoBuilder()
        .con_cliente("Karim")
        .con_producto("Laptop")
        .con_cantidad(2)
        .con_direccion("Mexico")
        .build()
    )

    assert pedido.cliente == "Karim"
    assert pedido.producto == "Laptop"
    assert pedido.cantidad == 2
    assert pedido.direccion == "Mexico"


def test_builder_devuelve_objeto_pedido():
    pedido = PedidoBuilder().con_cliente("Ana").build()

    assert pedido.__class__.__name__ == "Pedido"