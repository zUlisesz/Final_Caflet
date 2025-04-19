from datetime import date
from database.db_queries import Consulta
class Orden:
    
    def __init__(self, productos: list):
        self.productos  = productos
        
    def calcular_cuenta(self) -> int:
        total = 0 
        for producto in self.productos:
            total += producto.cantidad * producto.precio
        
        return total
        
    def preparar_envio(self) -> list:
        cuenta = self.calcular_cuenta()
        pedido_listo = [element.cantidad for element in self.productos ]
        pedido_listo.append(date.today())
        pedido_listo.append(cuenta)
        pedido_listo.append(False)
        
        return pedido_listo
    
    def limpiar_pedido(self) -> None:
        for element in self.productos:
            element.cantidad = 0 
            
    def agregar_productos(self, pedido) -> None:
        for element in pedido.rows:
            producto = element.data 
            try:
                cantidad = int(element.cells[1].content.value)
            except (ValueError, TypeError):
                cantidad = 0 
            for product in self.productos:
                if product.nombre == producto:
                    product.cantidad = cantidad
                    break
               
    def es_producible(self, materiales) -> bool:
        for material in materiales:
            if material[1] > material[0].cantidad:
                return False

        return True
    
    def cocinar(self, materiales):
        for material in materiales:
            ingrediente = material[0]
            cantidad = material[1]
            nuevo_valor = ingrediente.cantidad - cantidad
            ingrediente.cantidad = nuevo_valor
            Consulta.update_ingredientes(ingrediente.nombre, nuevo_valor)


            
        
        