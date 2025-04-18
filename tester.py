from data.productos import *
from models.orden import Orden

actual_orden = Orden(productos)

for element in actual_orden.productos:
    element.cantidad  =2
    
print(actual_orden.calcular_cuenta())