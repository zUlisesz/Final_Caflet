from data.objetos import *
from models.pedido import Pedido

def print_orden()-> None:
    for element in actual_orden.productos:
        print(element)
        
def print_pedidos() -> None:
    for element in Pedido.contenido:
        print(element)
        
