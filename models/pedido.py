from database.db_queries import Consulta
class Pedido:
    
    contenido = {}
    
    def __init__(self,id, pastel, flan, docena_galletas, brownie, americano, malteada, smoothie ,fecha, total, entregado):
        self.id = id
        self.pastel = pastel
        self.flan = flan
        self.docena_galletas = docena_galletas
        self.brownie = brownie
        self.americano = americano
        self.malteada = malteada
        self.smoothie = smoothie
        self.fecha =fecha
        self.total = total
        self.entregado = entregado
        Pedido.contenido[self.id] = self
        
    def __repr__(self):
        return f'Id: {self.id} - {self.fecha} - {self.total}'
      
    @classmethod  
    def cargar_pedidos(cls) -> None:
        cls.contenido.clear()
        for id, pastel, flan, docena_galletas, brownie, americano, malteada, smoothie ,fecha, total, entregado in Consulta.select_all_pedidos():
            Pedido(id, pastel, flan, docena_galletas, brownie, americano, malteada, smoothie, fecha, total, entregado)
      
    @classmethod  
    def cargar_ventas(cls) -> None:
        cls.contenido.clear()
        for id, pastel, flan, docena_galletas, brownie, americano, malteada, smoothie ,fecha, total, entregado in Consulta.all_ventas():
            Pedido(id, pastel, flan, docena_galletas, brownie, americano, malteada, smoothie, fecha, total, entregado)
            
    @classmethod
    def entregar_pedido(cls,id):
        cls.contenido.get(id).entregado = True
        Consulta.set_entregado(id)
        cls.cargar_pedidos()

        