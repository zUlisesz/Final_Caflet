import flet as ft
from views.components import *
from views.custom_controls import Box700x340, Box1460x345

def customerView(page: ft.Page):
    page.controls.clear()

    page.add(
        ft.Container(
            width=1480,
            height=720,
            margin=20,
            padding= ft.padding.symmetric(vertical= 10 , horizontal= 220),
            content=ft.Column(
                controls=[
                    Box1460x345(
                        height=290,
                        controls=[
                            Box700x340(control=Desserts_menu, height=285, aligment= ft.alignment.top_center),
                            Box700x340(control=Beverages_menu, height=285, padding= ft.alignment.top_center)
                        ]
                    ),
                    Box1460x345(
                        height=415,
                        espacios = 120 ,
                        controls=[
                            Box700x340(control= ft.Column(
                                spacing= 20,
                                width = 450, 
                                horizontal_alignment= ft.MainAxisAlignment.CENTER,
                                controls=[customer_title, instructions_label, boton_pedido]
                            ), padding= ft.padding.symmetric( horizontal= 10 , vertical= 20)),
                            caja_pedido,
                        ]
                    )
                ]
            )
        )
    )
