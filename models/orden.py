from datetime import date
class Orden:
    
    def __init__(self, productos: list):
        self.productos  = productos
        
    def calcular_cuenta(self):
        total = 0 
        for producto in self.productos:
            total += producto.cantidad * producto.precio
        
        return total
        
    def preparar_envio(self) -> None:
        cuenta = self.calcular_cuenta()
        pedido_listo = [element.cantidad for element in self.productos ]
        pedido_listo.append(date.today())
        pedido_listo.append(cuenta)
        
        return pedido_listo
    
    def limpiar_pedido(self):
        for element in self.productos:
            element.cantidad = 0 
        
        