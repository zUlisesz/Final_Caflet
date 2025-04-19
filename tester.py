from data.objetos import *
from models.pedido import Pedido
from database.db_queries import Consulta

def print_orden()-> None:
    for element in actual_orden.productos:
        print(element)
        
def print_pedidos() -> None:
    for element in Pedido.contenido:
        print(element)
        

def llenar_pedido():
    for element in actual_orden.productos:
        element.cantidad = 2
        
def print_inventario():
    for element in Ingrediente.inventario.values():
        print(element)
        

