import flet as ft
import matplotlib.pyplot as plt
import io
import base64
from database.db_queries import Consulta  # Asegúrate de tener la función que trae los datos

def estadisticasView(page: ft.Page):
    # Obtener datos desde la base de datos (reemplaza esta parte si usas otra función)
    datos = Consulta.top_productos()  # Debe devolver una lista de tuplas con (producto, cantidad)

    productos = [fila[0] for fila in datos]
    cantidades = [fila[1] for fila in datos]

    # Crear la gráfica de pastel
    fig, ax = plt.subplots()
    ax.pie(cantidades, labels=productos, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Hacer la gráfica circular

    # Guardar imagen en memoria
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()

    # Mostrar imagen en Flet
    page.controls.clear()
    page.add(
        ft.Container(
            margin=20,
            content=ft.Column([
                ft.Text("Productos más vendidos", size=24, weight="bold"),
                ft.Image(src_base64=img_base64, width=500, height=500),
            ], alignment=ft.MainAxisAlignment.START)
        )
    )
    page.update()
