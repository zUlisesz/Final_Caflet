import flet as ft

class Box700x340(ft.Container):
    def __init__(self, height= None , control = None, event = None, padding = None, page = None ):
        super().__init__(
            width= 700,
            height= 340 if height == None else height,
            content= control,
            border_radius= 12,
            padding = padding,
            alignment= ft.alignment.center,
            #shadow= ft.BoxShadow(
            #    blur_radius= 10,
            #    color = ft.Colors.BLACK87,
            #    offset= ft.Offset(4, 4),
            #),
            gradient= ft.LinearGradient(  
                begin= ft.alignment.top_center,
                end= ft.alignment.bottom_center,
                colors=[ft.Colors.LIME_ACCENT, ft.Colors.BLACK12],
            )
        )
        
class Box1460x345(ft.Container):
    def __init__(self, controls: list, height = None):
        super().__init__(
            width = 1460 ,
            height= 345 if height == None else height,
            padding = ft.padding.symmetric( vertical= 10 , horizontal=20 ) , 
            content= ft.Row(
                controls= controls
            )
        )
        
class Box400x500(ft.Container):
    def __init__(self, content = None, event = None):
        super().__init__(
            width= 440 ,
            height= 500,
            border_radius= 12,
            alignment= ft.alignment.center,
            content= content, 
            ink= True, 
            on_click= event
        )
        