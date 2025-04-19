import flet as ft 
from data.objetos import actual_orden
from models.ingrediente import Ingrediente
from database.db_queries import Consulta
from views.custom_controls import Box700x340

#funciones axuliares para manipular la tabla del pedido
def on_row_selected(e):
    order_table.visible = True
    row_name = e.control.data
    updated = False
    for row in order_table.rows:
        if row.data == row_name:
            t = int(row.cells[1].content.value)
            row.cells[1].content.value = str( t + 1)
            updated = True
            break

    if not updated:
        order_table.rows.append(
            ft.DataRow(
                data= row_name,
                cells=[
                    ft.DataCell(ft.Text(value=row_name.upper())),
                    ft.DataCell(ft.Text(value='1', width= 80 ,text_align= ft.TextAlign.CENTER))
                ]
            )
        )
    
    actual_orden.agregar_productos(order_table)
    order_table.update()
    
def reset_values(e = None) ->None:
    user_name.value = None
    user_password.value = None
    
def hacer_pedido(e) -> None:
    actual_orden.agregar_productos(order_table)
    Ingrediente.cargar_ingredientes()
    totales = Ingrediente.calcular_ingredientes_totales(actual_orden.productos)
    
    if actual_orden.es_producible(totales):
        actual_orden.cocinar(totales)
        Ingrediente.cargar_ingredientes()

        Consulta.send_pedido(actual_orden)
        
    else:
        not_enogh.visible = True
        
    order_table.visible = False 
    actual_orden.limpiar_pedido()
    order_table.rows.clear()
    order_table.update()
    
    

#fuente principal de todas de las cadenas de las vistas
fuente = 'Arial'

#imágenes de las vistas
admin_image = ft.Image(src="assets/admin.png",width=340,height=400,fit=ft.ImageFit.CONTAIN)
customer_image = ft.Image(src="assets/customer.png",width=340,height=400,fit=ft.ImageFit.CONTAIN)
ideas_image = ft.Image(src= 'ideas_4.png', width= 400, height= 400, fit  = ft.ImageFit.CONTAIN)

#letreros de las imágenes de las vista
admin_label = ft.Text(
    value = 'SIGN AS ADMINISTRATOR',
    font_family= fuente ,
    size= 28,
    width= 380,
    text_align= ft.TextAlign.CENTER
) 

customer_label  = ft.Text(
    value = 'SIGN AS CUSTOMER',
    font_family= fuente ,
    size= 28,
    width= 340,
    text_align= ft.TextAlign.CENTER
) 

ideas_label = ft.Text(
    value = '¿SE TE ANTOJA ALGO NUEVO?\nCUENTANOS',
    font_family= fuente ,
    size= 26,
    width= 400,
    text_align= ft.TextAlign.CENTER
) 

#componentes gráficos del menú de postres
Desserts_columns =[
    ft.DataColumn(ft.Text("POSTRE", font_family= fuente)),
    ft.DataColumn(ft.Text("SABORES", font_family= fuente)),
    ft.DataColumn(ft.Text("PRECIO", font_family= fuente)),
]

Desserts_rows =[
    ft.DataRow(
        data="rebanada de pastel",  
        on_select_changed= on_row_selected,
        cells=[
            ft.DataCell(ft.Text("REBANADA DE PASTEL", font_family= fuente)),
            ft.DataCell(ft.Text("TRES LECHES", font_family= fuente)),
            ft.DataCell(ft.Text("$ 60", font_family= fuente)),
        ],
    ),
    ft.DataRow(
        data="rebanada de flan",  
        on_select_changed= on_row_selected,
        cells=[
            ft.DataCell(ft.Text("REBANADA DE FLAN", font_family= fuente)),
            ft.DataCell(ft.Text("NAPOLITANO", font_family= fuente)),
            ft.DataCell(ft.Text("$ 60", font_family= fuente)),
        ],
    ),
    ft.DataRow(
        data="docena de galletas",  
        on_select_changed= on_row_selected,
        cells=[
            ft.DataCell(ft.Text("DOCENA DE GALLETAS", font_family= fuente)),
            ft.DataCell(ft.Text("ALMENDRAS", font_family= fuente)),
            ft.DataCell(ft.Text("$ 120", font_family= fuente)),
        ],
    ),
    ft.DataRow(
        data="brownie",  
        on_select_changed= on_row_selected,
        cells=[
            ft.DataCell(ft.Text("BROWNIE", font_family= fuente)),
            ft.DataCell(ft.Text("CHOCOLATE", font_family= fuente)),
            ft.DataCell(ft.Text("$ 80", font_family= fuente))
        ]
    )
]

Desserts_menu = ft.DataTable(
    heading_row_height= ft.FontWeight.W_400,
    border_radius= 12, 
    columns= Desserts_columns,
    rows= Desserts_rows
)

#componentes gráficos del menú de bebidas

beverages_columns = [
    ft.DataColumn(ft.Text("BEBIDA", font_family= fuente)),
    ft.DataColumn(ft.Text("SABORES", font_family= fuente)),
    ft.DataColumn(ft.Text("PRECIO", font_family= fuente), numeric=True),
]

beverages_rows = [
    ft.DataRow(
        data="café americano",  
        on_select_changed= on_row_selected,
        cells=[
            ft.DataCell(ft.Text("CAFÉ", font_family= fuente)),
            ft.DataCell(ft.Text("AMERICANO", font_family= fuente)),
            ft.DataCell(ft.Text("$ 40", font_family= fuente)),
        ],
    ),
    ft.DataRow(
        data="malteada de fresa",  
        on_select_changed= on_row_selected,
        cells=[
            ft.DataCell(ft.Text("MALTEADA", font_family= fuente)),
            ft.DataCell(ft.Text("FRESA", font_family= fuente)),
            ft.DataCell(ft.Text("$ 50", font_family= fuente)),
        ],
    ),
    ft.DataRow(
        data="smoothie de mora azul",  
        on_select_changed= on_row_selected,
        cells=[
            ft.DataCell(ft.Text("SMOOTHIE", font_family= fuente)),
            ft.DataCell(ft.Text("MORA AZUL", font_family= fuente)),
            ft.DataCell(ft.Text("$ 60", font_family= fuente)),
        ],
    )
]

Beverages_menu = ft.DataTable(
    heading_row_height= ft.FontWeight.W_400,
    border_radius= 12,
    columns= beverages_columns,
    rows= beverages_rows
)

#componentes gráficos de la tabla de pedido

order_columns = [
    ft.DataColumn(ft.Text("PRODUCTO", font_family= fuente, weight= ft.FontWeight.W_400)),
    ft.DataColumn(ft.Text("CANTIDAD", font_family= fuente,weight =  ft.FontWeight.W_400))
]

order_table = ft.DataTable(
    heading_row_height= ft.FontWeight.W_400,
    border_radius= 12,
    visible= False ,
    columns= order_columns,
    rows = []
)

#Entradas de texto de validación
user_name =ft.TextField(label = 'NOMBRE DE USUARIO', width= 300,border_radius= 12)
user_password = ft.TextField(label = 'CONTRASEÑA', width= 300, border_radius= 12, password= True)

#Alertas emergentes

not_found = ft.AlertDialog(
    content= ft.Text(value = f'USUARIO {user_name.value} NO EXISTENTE', font_family= fuente)
)

wrong_password = ft.AlertDialog(
    content= ft.Text(value = f'LA CONTRASEÑA {user_password.value} ES INCORRECTA', font_family= fuente)
)

empty_fields  = ft.AlertDialog(
    content= ft.Text(value = 'ASEGURESE DE LLENAR TODOS LOS CMPOS', font_family= fuente)
)

not_enogh = ft.Text(
    value = 'SETIMOS INFORMALE QUE NO CONTAMOS CON TODOS LOS INGREDIENTES PARA SATISFACER SU PEDIDO',
    font_family= fuente,
    visible= False
) 

log_in = ft.BottomSheet(
    content= ft.Container(
        width= 500,
        height= 240,
        alignment= ft.alignment.center,
        padding= 30,
        content= ft.Column(
            spacing= 20,
            controls= [
                user_name, user_password,
                ft.ElevatedButton(text= 'ACCEDER', width= 300)
            ]
        )     
    ),
    dismissible= True,
    on_dismiss= reset_values,
    elevation= 10 
)

#letreros y botones para la vistas

titulo_cafeteria = ft.Text(value = 'BIENVENIDO A LA CAFETERÍA' , size=40 , font_family = fuente)
customer_title = ft.Text(value = 'CREANDO MI PEDIDO', size=30,font_family= fuente) 
instructions_label = ft.Text( value = '''PARA CREAR TU PEDIDO SOLO HAZ CLICK SOBRE EL PRODUCTO QUE
QUE DESEAS ODERNAR EN LOS MENÚS DE LA PARTE SUPERIOR Y SELECCIONA DESDE DONDE NOS VISITAS''',
font_family= fuente, size= 10)

total_account = ft.Text(value = 'TOTAL A PAGAR = $ 0', font_family= fuente, size= 10 )

boton_pedido = ft.ElevatedButton(
    text= 'HACER PEDIDO',
    width= 200 ,
    elevation= 30,
    on_click= hacer_pedido
)

caja_pedido = Box700x340(
    control= ft.Row (
        controls= [
            order_table,
            not_enogh
        ]  
    ), 
    height=410
)
