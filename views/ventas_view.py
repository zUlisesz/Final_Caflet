import flet as ft
from database.db_queries import Consulta
from views.components import  opciones, ventas_table, ventas_title

def ventasView(page:ft.Page):
    from views.admin_view import administradorView
    
    icon_back = ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_size= 50, on_click= lambda e: administradorView(page)) 
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
        contenido = ()
        if selector.value == 'TODAS LAS VENTAS':
            contenido = Consulta.all_ventas()
        elif selector.value == 'VENTAS DE ESTE DÍA':
            contenido = Consulta.ventas_dia_actual()
        elif selector.value == 'VENTAS DE ESTA SEMANA':
            contenido = Consulta.ventas_semana_actual()
        elif selector.value == 'VENTAS DE ESTE MES':
            contenido = Consulta.ventas_mes_actual()
        elif selector.value == 'VENTAS DE ESTE AÑO':
            contenido = Consulta.ventas_año_actual()
        
        ventas_table.rows = [
            ft.DataRow(
                cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]
            )
            for row in contenido
        ]
        
        ventas_table.update()
        
        
        
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
                        spacing = 30 ,
                        controls= [
                            ventas_title,
                            selector,
                            icon_back, 
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