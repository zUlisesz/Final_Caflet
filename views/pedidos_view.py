import flet as ft
from models.pedido import Pedido
from database.db_queries import Consulta
from views.components import pedidos_table, fuente

def pedidosView(page: ft.Page):
    from views.admin_view import administradorView
    def on_row(e):
        id = e.control.data
        def entregar(e):
            Consulta.set_entregado(int(id))
            Pedido.cargar_pedidos()
            pedidos_table.rows = [
                ft.DataRow(
                    data = row[0],
                    on_select_changed= on_row,
                    cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]
                )
                for row in Consulta.productos_pedidos()
            ]
            page.close(marcar)
            page.update()
            
        marcar = ft.BottomSheet(
            content= ft.Container(
                width= 500,
                height= 200,
                alignment= ft.alignment.center,
                padding= 40,
                content= ft.Column(
                    spacing= 20,
                    controls= [
                        ft.Text(f'MARCAR COMO ENTREGADO PEDIDO NÚMERO: {id}', font_family= fuente, size= 16),
                        ft.ElevatedButton(text= 'MARCAR COMO ENTREGADO', width= 380, on_click= entregar, height= 60)
                    ]
                )     
            ),
            dismissible= True,
            elevation= 10 
        )
        page.open(marcar)
        
    page.controls.clear()
    Pedido.cargar_pedidos()
    pedidos_table.rows = [
        ft.DataRow(
            data = row[0],
            on_select_changed= on_row,
            cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]
        )
        for row in Consulta.productos_pedidos()
    ]
    page.add(
        ft.Container(
            margin= 30 ,
            border_radius= 12,
            padding= ft.padding.symmetric(horizontal= 120, vertical= 60),
            content= ft.Row(
                spacing= 160,
                controls= [
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_size= 100, on_click= lambda e: administradorView(page)),
                    ft.Container(
                        border_radius= 12,
                        alignment= ft.alignment.top_center,
                        content= pedidos_table
                    )
                ]
            )
        )
    )
