from data.objetos import *
from models.pedido import Pedido
from database.db_queries import Consulta

def print_orden()-> None:
    for element in actual_orden.productos:
        print(element)
        
def print_pedidos() -> None:
    for element in Pedido.contenido.values():
        print(element)
        

def llenar_pedido():
    for element in actual_orden.productos:
        element.cantidad = 2
        
def print_inventario():
    for element in Ingrediente.inventario.values():
        print(element)
        
import flet as ft

def main(page: ft.Page):
    colors = [
        ft.Colors.RED,
        ft.colors.BLUE,
        ft.Colors.YELLOW,
        ft.Colors.PURPLE,
        ft.Colors.LIME,
    ]

    def get_options():
        options = []
        for color in colors:
            options.append(
                ft.DropdownOption(
                    key=color.value,
                    content=ft.Text(
                        value=color.value,
                        color=color,
                    ),
                )
            )
        return options

    def dropdown_changed(e):
        e.control.color = e.control.value
        page.update()

    dd = ft.Dropdown(
        editable=True,
        label="Color",
        options=get_options(),
        on_change=dropdown_changed,
    )

    page.add(dd)


ft.app(main)
