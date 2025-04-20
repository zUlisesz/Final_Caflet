import flet as ft
from views.components import stats_image, fuente
from views.ingredientes_view import ingredientesView
def administradorView(page: ft.Page):
    from views.main_view import mainView
    page.controls.clear()
    page.add(
        ft.Container(
            margin= 20 ,
            padding= ft.padding.symmetric(vertical= 20  , horizontal= 60),
            content= ft.Row(
                spacing= 100 ,
                controls= [
                    ft.Container(
                        width = 600 ,
                        height = 600 ,
                        padding= ft.padding.symmetric(vertical= 20 , horizontal= 50),
                        alignment= ft.alignment.center_left,
                        content= ft.Column(
                            spacing= 42,
                            controls= [
                                ft.Text('BIENVENIDO ADMINISTRADOR', size= 30, font_family= fuente, weight= ft.FontWeight.W_700),
                                ft.ElevatedButton(text= 'REVISAR PEDIDOS', elevation= 20, width= 340, height= 60),
                                ft.ElevatedButton(text= 'REVISAR INGREDIENTES', elevation= 20, width= 340, height= 60, on_click= lambda e: ingredientesView(page)),
                                ft.ElevatedButton(text= 'REVISAR VENTAS', elevation= 20, width= 340, height= 60),
                                ft.ElevatedButton(text= 'REVISAR ESTADÍSTICAS', elevation= 20, width= 340, height= 60),
                                ft.ElevatedButton(text= 'VOLVER AL INCIO', elevation= 20, width= 340, height= 60, on_click= lambda e: mainView(page))
                            ]
                        )
                    ),
                    ft.Container(
                        alignment = ft.alignment.center, 
                        content= stats_image 
                    )
                ]
            )
        )
    )
    
    page.update()