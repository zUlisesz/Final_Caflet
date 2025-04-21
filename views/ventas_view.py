import flet as ft
from database.db_queries import Consulta
from views.components import  opciones, ventas_table, ventas_title

def ventasView(page:ft.Page):
    from views.admin_view import administradorView
    page.controls.clear()
    def get_options() -> list:
        options = []
        for opcion in opciones:
            options.append(
                ft.DropdownOption(
                    key= opcion,
                    content=ft.Text(
                        value= opcion,
                    ),
                )
            )
        return options
    
    def seleccionar(e)-> None:
        print(type(e))
        
    ventas_table.rows = [
        ft.DataRow(
            cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]
        )
        for row in Consulta.all_ventas()
    ]
        
    selector = ft.Dropdown(
        label= 'TIPO DE VENTAS',
        width= 300,
        elevation= 20 ,
        editable= True,
        options= get_options(),
        on_change= seleccionar
    )
    
    page.add(
        ft.Container(
            border_radius= 12,
            padding= ft.padding.symmetric( vertical= 50 , horizontal=160),
            content= ft.Column(
                spacing= 30 ,
                controls=[
                    ft.Row(
                        spacing = 60 ,
                        controls= [
                            ventas_title,
                            selector,
                            ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_size= 50, on_click= lambda e: administradorView(page))
                        ]
                    ),
                    ft.Container(
                        border_radius= 12,
                        content= ventas_table
                    )
                ]
            )
        )
    )