import flet as ft
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import io
import base64
from database.db_queries import Consulta
import views.components as cp

def estadisticasView(page: ft.Page):
    from views.admin_view import administradorView
    datos = Consulta.top_productos()

    productos = [fila[0] for fila in datos]
    cantidades = [fila[1] for fila in datos]

    fig, ax = plt.subplots()
    ax.pie(cantidades, labels=productos, autopct='%1.1f%%', startangle=90,)
    ax.axis('equal')  

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    grafica = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()

    page.controls.clear()
    page.add(
        ft.Container(
            margin=10,
            padding= ft.padding.symmetric(horizontal= 140, vertical= 60 ),
            content=ft.Column(
                spacing= 0,
                controls= [
                    cp.estadisticas_title ,
                    ft.Row(
                        spacing = 100 ,
                        controls=[
                            ft.Container(
                                ft.Column(
                                    spacing = 36,
                                    controls=[
                                        cp.label_ventas_hoy,
                                        cp.label_ventas_semana,
                                        cp.label_ventas_mes,
                                        cp.label_ventas_año,
                                        cp.label_ventas_totales,
                                        ft.ElevatedButton(
                                            text= 'CREAR PDF',
                                            width= 300, height= 50
                                        ),
                                        ft.ElevatedButton(
                                            text= 'VOLVER A ADMINISTRADOR',
                                            width= 300, height= 50,
                                            on_click= lambda e: administradorView(page)
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                content= ft.Image(src_base64= grafica, width=800, height=800)
                            )
                        ]
                    )
                ], 
                alignment=ft.alignment.center
            )
        )
    )
    page.update()
