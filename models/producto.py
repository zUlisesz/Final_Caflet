class Producto:
    def __init__(self ,nombre, precio, ingredientes:list):
        self.nombre = nombre
        self.cantidad = 0
        self.precio = precio 
        self.ingredientes = ingredientes
        
    def __repr__(self):
        return f'{self.nombre} - {self.cantidad} - {self.precio}'

    def es_cocinable(self) -> bool:
        for ingrediente, minimos in self.ingredientes:
            if minimos > ingrediente.cantidad:
                return False

        return True
                