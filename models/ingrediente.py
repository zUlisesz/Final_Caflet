from database.db_queries import Consulta
class Ingrediente:
    inventario = {}
    def __init__(self, nombre, cantidad, minimo , maximo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.minimo = minimo
        self.maximo = maximo
        Ingrediente.inventario[self.nombre] = self
        
    def __repr__(self):
        return f'{self.nombre} - {self.cantidad}'
        
    @classmethod
    def get(cls, nombre) :
        return cls.inventario.get(nombre.upper())
    
    @classmethod
    def cargar_ingredientes(cls):
        for nombre, cantidad, minn, maxx in Consulta.all_ingredientes():
            Ingrediente(nombre , cantidad, minn , maxx)