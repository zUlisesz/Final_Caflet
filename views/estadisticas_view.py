import flet as ft
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from database.db_queries import Consulta
import views.components as cp

def crear_pdf_estadisticas(ventas_hoy, ventas_semana, ventas_mes, ventas_ano, ventas_totales, imagen_base64):
    nombre_archivo = f"Estadisticas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 50, "Estadísticas de Ventas - Cafetería")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Ventas del día: {ventas_hoy}")
    c.drawString(50, height - 120, f"Ventas de la semana: {ventas_semana}")
    c.drawString(50, height - 140, f"Ventas del mes: {ventas_mes}")
    c.drawString(50, height - 160, f"Ventas del año: {ventas_ano}")
    c.drawString(50, height - 180, f"Ventas totales: {ventas_totales}")

    image_path = "grafica_temp.png"
    with open(image_path, "wb") as f:
        f.write(base64.b64decode(imagen_base64))
    c.drawImage(image_path, 50, height - 500, width=500, preserveAspectRatio=True)

    c.save()
    print(f"PDF guardado como {nombre_archivo}")
    os.remove(image_path)

def estadisticasView(page: ft.Page):
    from views.admin_view import administradorView
    datos = Consulta.top_productos()

    productos = [fila[0] for fila in datos]
    cantidades = [fila[1] for fila in datos]

    fig, ax = plt.subplots()
    ax.pie(cantidades, labels=productos, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    grafica = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()

    ventas_hoy = cp.label_ventas_hoy.value
    ventas_semana = cp.label_ventas_semana.value
    ventas_mes = cp.label_ventas_mes.value
    ventas_ano = cp.label_ventas_año.value
    ventas_totales = cp.label_ventas_totales.value

    page.controls.clear()
    page.add(
        ft.Container(
            margin=20,
            padding=ft.padding.symmetric(horizontal=50, vertical=40),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=40,
                controls=[
                    cp.estadisticas_title,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Container(
                                content=ft.Card(
                                    content=ft.Container(
                                        padding=20,
                                        width=400,
                                        content=ft.Column(
                                            spacing=20,
                                            controls=[
                                                cp.label_ventas_hoy,
                                                cp.label_ventas_semana,
                                                cp.label_ventas_mes,
                                                cp.label_ventas_año,
                                                cp.label_ventas_totales,
                                            ]
                                        )
                                    )
                                )
                            ),
                            ft.Container(
                                content=ft.Image(src_base64=grafica, width=500, height=500),
                                padding=ft.padding.only(top=10),
                            )
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=40,
                        controls=[
                            ft.ElevatedButton(
                                text="CREAR PDF",
                                width=200,
                                height=50,
                                on_click=lambda e: crear_pdf_estadisticas(
                                    ventas_hoy, ventas_semana, ventas_mes,
                                    ventas_ano, ventas_totales, grafica
                                )
                            ),
                            ft.ElevatedButton(
                                text="VOLVER A ADMINISTRADOR",
                                width=220,
                                height=50,
                                on_click=lambda e: administradorView(page)
                            )
                        ]
                    )
                ]
            )
        )
    )
    page.update()
