import flet as ft 
from views.components import ingredientes_table
from database.db_queries import Consulta

def ingredientesView(page: ft.Page):
    page.controls.clear()
    ingredientes_table.rows = [
        ft.DataRow(
            cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]
        )
        for row in Consulta.all_ingredientes()
    ]

    page.add(
        ingredientes_table
    )