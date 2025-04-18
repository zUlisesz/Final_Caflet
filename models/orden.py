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
        self.productos.append(date.today())
        
        