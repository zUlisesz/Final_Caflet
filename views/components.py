import flet as ft 
from data.objetos import actual_orden
from models.ingrediente import Ingrediente
from database.db_queries import Consulta
from views.custom_controls import Box700x340

#funciones axuliares para manipular la tabla del pedido
def on_row_selected(e):
    caja_pedido.content = order_table
    order_table.visible = True
    caja_pedido.alignment = ft.alignment.top_center
    
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
    letrero.value = f'TOTAL DE TU CUENTA: {actual_orden.calcular_cuenta()}'
    letrero.update()
    
    
    caja_pedido.update()
    actual_orden.agregar_productos(order_table)
    order_table.update()
    
def reset_values(e = None) ->None:
    user_password.value = None
    
def hacer_pedido(e) -> None:
    
    if not len(order_table.rows) == 0:
        actual_orden.agregar_productos(order_table)
        Ingrediente.cargar_ingredientes()
        totales = Ingrediente.calcular_ingredientes_totales(actual_orden.productos)
        caja_pedido.alignment = ft.alignment.center
        if actual_orden.es_producible(totales):
            actual_orden.cocinar(totales)
            Ingrediente.cargar_ingredientes()
            Consulta.send_pedido(actual_orden)
            caja_pedido.content = successfuly_done
            
        else:
            caja_pedido.content = not_enogh
            
        letrero.value = instrucciones
        letrero.update()
        actual_orden.limpiar_pedido()
        order_table.rows.clear()
        caja_pedido.update()
    
    

#fuente principal de todas de las cadenas de las vistas
fuente = 'Arial'

#imágenes de las vistas
admin_image = ft.Image(src="assets/admin.png",width=340,height=400,fit=ft.ImageFit.CONTAIN)
customer_image = ft.Image(src="assets/customer.png",width=340,height=400,fit=ft.ImageFit.CONTAIN)
ideas_image = ft.Image(src= 'assets/ideas_4.png', width= 400, height= 400, fit  = ft.ImageFit.CONTAIN)

stats_image = ft.Image(src = 'assets/stats.png', width= 660,height= 660 , fit = ft.ImageFit.CONTAIN)

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
    ft.DataColumn(ft.Text("POSTRE", font_family= fuente, weight= ft.FontWeight.W_500)),
    ft.DataColumn(ft.Text("SABORES", font_family= fuente, weight= ft.FontWeight.W_500)),
    ft.DataColumn(ft.Text("PRECIO", font_family= fuente, weight= ft.FontWeight.W_500)),
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
    heading_row_color= ft.Colors.GREY_200,
    border_radius= 12, 
    columns= Desserts_columns,
    rows= Desserts_rows
)

#componentes gráficos del menú de bebidas

beverages_columns = [
    ft.DataColumn(ft.Text("BEBIDA", font_family= fuente, weight= ft.FontWeight.W_500)),
    ft.DataColumn(ft.Text("SABORES", font_family= fuente,  weight= ft.FontWeight.W_500)),
    ft.DataColumn(ft.Text("PRECIO", font_family= fuente,  weight= ft.FontWeight.W_500)),
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
    heading_row_color= ft.Colors.GREY_200,
    heading_row_height= ft.FontWeight.W_400,
    border_radius= 12,
    columns= beverages_columns,
    rows= beverages_rows
)

#componentes gráficos de la tabla de pedido

order_columns = [
    ft.DataColumn(ft.Text("PRODUCTO", font_family= fuente, weight= ft.FontWeight.W_500)),
    ft.DataColumn(ft.Text("CANTIDAD", font_family= fuente,weight =  ft.FontWeight.W_500))
]

order_table = ft.DataTable(
    heading_row_color= ft.Colors.GREY_200,
    border_radius= 12,
    visible= False ,
    columns= order_columns,
    rows = []
)

#componentes gráficos de la tabla de ingredientes

ingredientes_columns = [
    ft.DataColumn(ft.Text('NOMBRE', font_family= fuente)),
    ft.DataColumn(ft.Text('CANTIDAD', font_family= fuente)),
    ft.DataColumn(ft.Text('MÍNIMOS', font_family= fuente)),
    ft.DataColumn(ft.Text('MÁXIMOS', font_family= fuente)),
]

ingredientes_table = ft.DataTable(
    heading_row_color= ft.Colors.GREY_200,
    border_radius= 12,
    columns= ingredientes_columns,
    rows= []
)

#componente gráficos de la tabla de pedidos
pedidos_columns=[
    ft.DataColumn(ft.Text(value = 'ID', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'PASTEL', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'FLAN', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'GALLETAS', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'BROWNIE', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'AMERICANO', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'MALTEADA', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'SMOOTHIE', font_family= fuente)),
]

pedidos_table = ft.DataTable(
    heading_row_color= ft.Colors.GREY_200,
    
    border_radius= 12,
    show_bottom_border= True,
    columns= pedidos_columns,
    rows= []
)

#componentes gráficos de la tabla de ventas
ventas_columns=[
    ft.DataColumn(ft.Text(value = 'ID', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'PASTEL', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'FLAN', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'GALLETAS', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'BROWNIE', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'AMERICANO', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'MALTEADA', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'SMOOTHIE', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'FECHA', font_family= fuente)),
    ft.DataColumn(ft.Text(value = 'TOTAL', font_family= fuente)),
]

ventas_table = ft.DataTable(
    heading_row_color= ft .Colors.GREY_200,
    border_radius= 12,
    columns= ventas_columns,
    rows= []
)

#Entradas de texto de validación
user_password = ft.TextField(label = 'CONTRASEÑA', width= 300, border_radius= 12, password= True)

#Alertas emergentes

wrong_password = ft.AlertDialog(
    content= ft.Text(value = f'LA CONTRASEÑA {user_password.value} ES INCORRECTA', font_family= fuente)
)

empty_fields  = ft.AlertDialog(
    content= ft.Text(value = 'ASEGURESE DE LLENAR TODOS LOS CMPOS', font_family= fuente)
)

not_enogh = ft.Text(
    value = 'SENTIMOS INFORMALE QUE:\nNO CONTAMOS CON TODOS LOS INGREDIENTES PARA SATISFACER SU PEDIDO',
    font_family= fuente,
    weight= ft.FontWeight.W_500,
    size= 20 
) 

successfuly_done = ft.Text(
    value = 'PEDIDO REALIZADO CON ÉXITO,\nLISTO EN APROXIMADAMENTE\n20 MINUTOS',
    font_family= fuente,
    size= 20 ,
    weight= ft.FontWeight.W_500,
    text_align= ft.TextAlign.CENTER
)

log_in = ft.BottomSheet(
    content= ft.Container(
        width= 500,
        height= 200,
        alignment= ft.alignment.center,
        padding= 30,
        content= ft.Column(
            spacing= 20,
            controls= [
                user_password,
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


instrucciones = '''PARA CREAR TU PEDIDO HAZ CLICK SOBRE EL PRODUCTO QUE
QUE DESEAS ODERNAR EN LOS MENÚS'''

letrero = ft.Text( value = instrucciones, font_family= fuente, size= 16)

boton_pedido = ft.ElevatedButton(
    text= 'HACER PEDIDO',
    width= 300 ,
    elevation= 20,
    on_click= hacer_pedido
)

caja_pedido = Box700x340(
    control= order_table,
    aligment= ft.alignment.top_center
)


opciones =[
    'TODAS LAS VENTAS',
    'VENTAS DE ESTE DÍA',
    'VENTAS DE ESTA SEMANA',
    'VENTAS DE ESTE MES',
    'VENTAS DE ESTE AÑO'
]

ventas_title = ft.Text(
    value = 'QUE TÁL GERENTE, ÉSTAS SON NUESTRAS VENTAS',
    font_family= fuente,
    size= 30
)

estadisticas_title = ft.Text("ESTOS SON LOS DATOS MÁS IMPORTANTES A CONOCER", size=30, font_family= fuente)
label_ventas_hoy = ft.Text(value = F'ESTE DÍA HAS VENDIDO: $ {Consulta.sum_hoy()}', size=18 , font_family= fuente)
label_ventas_semana = ft.Text(value = F'ESTA SEMANA HAS VENDIDO: $ {Consulta.sum_semana()}', size=18 , font_family= fuente)
label_ventas_mes = ft.Text(value = F'ESTE MES HAS VENDIDO: $ {Consulta.sum_mes()}', size=18 , font_family= fuente)
label_ventas_año = ft.Text(value = F'ESTE AÑO HAS VENDIDO: $ {Consulta.sum_año()}', size=18 , font_family= fuente)
label_ventas_totales = ft.Text(value = F'TUS VENTAS TOTALES SON DE: $ {Consulta.sum_total()}', size=18 , font_family= fuente)
