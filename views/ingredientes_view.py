import flet as ft 
from views.components import ingredientes_table, fuente
from database.db_queries import Consulta
from models.ingrediente import Ingrediente

def ingredientesView(page: ft.Page):
    from views.admin_view import administradorView
    page.controls.clear()
    ingredientes_table.rows = [
        ft.DataRow(
            cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]
        )
        for row in Consulta.all_ingredientes()
    ]
    
    def llenar_inventario(e)->None:
        Ingrediente.llenar_invetario()
        ingredientes_table.rows = [
            ft.DataRow(
                cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]
            )
            for row in Consulta.all_ingredientes()
        ]
        ingredientes_table.update()
        

    page.add(
        ft.Container(
            margin= 30 ,
            padding= ft.padding.symmetric(vertical= 10 , horizontal= 100),
            alignment= ft.alignment.top_center,
            content= ft.Row(
                spacing= 200,
                alignment= ft.alignment.top_center,
                controls= [
                    ft.Container( 
                        height= 860,
                        alignment= ft.alignment.top_center,
                        content= ft.Column(
                            spacing = 50,
                            controls=[
                                ft.Text(value = 'INVENTARIO DE INGREDIENTES', font_family= fuente ,size= 26),
                                ft.ElevatedButton(text = 'RELLENAR INVENTARIO', width= 400, height= 50, on_click= llenar_inventario),
                                ft.ElevatedButton(text = 'REGRESAR A ADMINISTRADOR', width= 400, height= 50, on_click= lambda e: administradorView(page))
                            ]
                        )
                    ),
                    ft.Container(
                        content= ingredientes_table,
                        border_radius= 12,
                        alignment= ft.alignment.top_center
                    )
                ]
            )
        )
    )