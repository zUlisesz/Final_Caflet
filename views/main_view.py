import flet as ft
from views.custom_controls import Box400x500
from views.customer_view import customerView
from views.requests_view import requests_view
from views.admin_view import administradorView
import views.components as cp

def mainView(page: ft.Page):
    page.controls.clear()
    page.scroll = True
    page.adaptive = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = 'CAFLETERÍA'


    def call_login(e) -> None:
        cp.log_in.content.content.controls[1].on_click = validation
        page.open(cp.log_in)

    def validation(e):
        if cp.user_password != None:
            if cp.user_password.value.strip() == 'pass':
                page.close(cp.log_in)
                administradorView(page)
            else:
                page.open(cp.wrong_password)         
        else:
            page.open(cp.empty_fields)

        cp.reset_values()

    page.add(
        ft.Container(
            width=1380,
            height=200,
            border_radius=12,
            margin=12,
            alignment=ft.alignment.center,
            content= cp.titulo_cafeteria,
        ),
        ft.Container(
            width=1480,
            height=520,
            padding= ft.padding.symmetric(vertical=2, horizontal=50),
            content=ft.Row(
                spacing=30,
                controls=[
                    Box400x500(content= ft.Column(
                        controls=[cp.logo_image, cp.logo_label]
                    )),
                    Box400x500(event=call_login, content= ft.Column(
                        controls=[cp.admin_image, cp.admin_label]
                    )),
                    Box400x500(event=lambda e: customerView(page), content= ft.Column(
                        controls=[cp.customer_image, cp.customer_label]
                    ))
                ]
            )
        )
    )