class Producto:
    def __init__(self ,nombre, cantidad, precio, ingredientes):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio 
        self.ingredientes = ingredientes
        
    def __repr__(self):
        return f'{self.nombre} - {self.cantidad} - {self.precio}'

    ##
    def es_cocinable(self):
        for ingredient, required_qty in self.ingredientes:
            if required_qty > ingredient.quantity:
                return False

        return True