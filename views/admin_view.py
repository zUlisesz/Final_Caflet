import flet as ft
from views.components import stats_image
def administradorView(page: ft.Page):
    page.controls.clear()
    page.add(
        ft.Container(
            content= ft.Text('BIENVENIDO ADMINISTRADOR')
        ),
        ft.Container(
            content= ft.Row(
                controls= [
                    ft.Container(
                        bgcolor= ft.Colors.BLUE_100
                    ),
                    ft.Container(
                        content= stats_image 
                    )
                ]
            )
        )
    )
    
    page.update()