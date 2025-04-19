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
            
    @classmethod
    def calcular_ingredientes_producto(cls, producto)-> list:
        medida = producto.ingredientes
        for ingrediente in medida:
            ingrediente[1] *= producto.cantidad
            
        return medida
    
    @classmethod
    def calcular_ingredientes_totales(cls, productos: list) -> list:
        ingredientes_totales = {}

        for producto in productos:
            medida = cls.calcular_ingredientes_producto(producto)
            for ingrediente, cantidad in medida:
                if ingrediente in ingredientes_totales:
                    ingredientes_totales[ingrediente] += cantidad
                else:
                    ingredientes_totales[ingrediente] = cantidad

        return [[ingrediente, cantidad] for ingrediente, cantidad in ingredientes_totales.items()]
            
            
        
            