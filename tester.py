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
        element.cantidad = 15
        
llenar_pedido()

totales =Ingrediente.calcular_ingredientes_totales(actual_orden.productos)

print(actual_orden.es_producible(totales))
