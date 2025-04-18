class Ingrediente:
    inventario = {}
    def __init__(self, nombre, cantidad, minimo , maximo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.minimo = minimo
        self.maximo = maximo
        Ingrediente.inventario[self.name] = self
        
    @classmethod
    def get(cls, nombre) :
        return cls.inventario.get(nombre.upper())