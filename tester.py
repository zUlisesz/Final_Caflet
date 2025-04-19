from data.objetos import *
from models.pedido import Pedido

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
        
print_inventario()
#Ingrediente.llenar_invetario()
#print('Lennado el inventario. . . . . ')
#print_inventario()
