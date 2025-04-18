from data.objetos import *
    
def print_orden()-> None:
    for element in actual_orden.productos:
        print(element)
        
print_orden()
for element in actual_orden.productos:
    element.cantidad = 3
    
print_orden()

print('limpiadno orden....')
actual_orden.limpiar_pedido()
print_orden()
    