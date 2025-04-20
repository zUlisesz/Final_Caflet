import flet as ft
from models.pedido import Pedido
from database.db_queries import Consulta
from views.components import pedidos_table, fuente

def pedidosView(page: ft.Page):
    page.controls.clear()
    Pedido.cargar_pedidos()
    pedidos_table.rows = [
        ft.DataRow(
            cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]
        )
        for row in Consulta.productos_pedidos()
    ]
    page.add(
        ft.Container(
            margin= 30 ,
            padding= 20 ,
            border_radius= 12,
            alignment= ft.alignment.top_center,
            content= pedidos_table
        )
    )
