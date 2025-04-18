import flet as ft

def administradorView(page: ft.Page):
    page.controls.clear()
    page.add(
        ft.Text( value = 'Bienvenido administrador')
    )