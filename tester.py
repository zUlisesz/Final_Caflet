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
    page.title = "Tabla con Checkboxes"
    page.scroll = True

    seleccionados = set()  # Guardará los IDs o índices seleccionados

    # Datos de ejemplo
    datos = [
        {"id": 1, "nombre": "Harina", "cantidad": "2 kg"},
        {"id": 2, "nombre": "Azúcar", "cantidad": "1 kg"},
        {"id": 3, "nombre": "Huevos", "cantidad": "12 unidades"},
    ]

    def checkbox_changed(e, item_id):
        if e.control.value:
            seleccionados.add(item_id)
        else:
            seleccionados.discard(item_id)
        print("Seleccionados:", seleccionados)

    # Construcción dinámica de filas
    filas = []
    for item in datos:
        checkbox = ft.Checkbox(value=False)
        checkbox.on_change = lambda e, item_id=item["id"]: checkbox_changed(e, item_id)

        fila = ft.DataRow(
            cells=[
                ft.DataCell(checkbox),
                ft.DataCell(ft.Text(item["nombre"])),
                ft.DataCell(ft.Text(item["cantidad"])),
            ]
        )
        filas.append(fila)

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Seleccionar")),
            ft.DataColumn(label=ft.Text("Ingrediente")),
            ft.DataColumn(label=ft.Text("Cantidad")),
        ],
        rows=filas,
    )

    page.add(tabla)

ft.app(target=main)
