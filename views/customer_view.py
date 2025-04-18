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
            padding=10,
            content=ft.Column(
                controls=[
                    Box1460x345(
                        height=290,
                        controls=[
                            Box700x340(control=Desserts_menu, height=285),
                            Box700x340(control=Beverages_menu, height=285)
                        ]
                    ),
                    Box1460x345(
                        height=415,
                        controls=[
                            Box700x340(control= ft.Column(
                                spacing=10,
                                horizontal_alignment= ft.MainAxisAlignment.CENTER,
                                controls=[customer_title, instructions_label, total_account]
                            ), padding=60),
                            Box700x340(control=order_table, height=410)
                        ]
                    )
                ]
            )
        )
    )
    
ft.app(target = customerView)