from models.ingrediente import Ingrediente
from models.producto import Producto

Ingrediente.cargar_ingredientes()

cake_Ingredientes =[
    [Ingrediente.get('harina de trigo'), 30],
    [Ingrediente.get('huevos'),1],
    [Ingrediente.get('azúcar'),25],
    [Ingrediente.get('leche evaporada'), 30],
    [Ingrediente.get('leche condensada'), 20],
    [Ingrediente.get('crema para batir'), 25],
    [Ingrediente.get('vainilla'),2]
]

flan_Ingredientes = [
    [Ingrediente.get('leche condensada'), 40 ],
    [Ingrediente.get('leche evaporada'), 40],
    [Ingrediente.get('huevos'), 1],
    [Ingrediente.get('queso crema'), 20],
    [Ingrediente.get('vainilla'), 2],
    [Ingrediente.get('azúcar'), 10]
]

brownie_Ingredientes = [
    [Ingrediente.get('harina de trigo'), 25],
    [Ingrediente.get('huevos'), 1],
    [Ingrediente.get('cacao en polvo'),10],
    [Ingrediente.get('azúcar'), 30],
    [Ingrediente.get('mantequilla'),20],
    [Ingrediente.get('vainilla'), 2]
]

cookies_Ingredientes = [
    [Ingrediente.get('harina de trigo'), 120],
    [Ingrediente.get('huevos'),1],
    [Ingrediente.get('mantequilla'), 80],
    [Ingrediente.get('azúcar'),30],
    [Ingrediente.get('vainilla'), 5]
]

amirican_Ingredientes =[
    [Ingrediente.get('café'), 15],
    [Ingrediente.get('agua'), 200],
    [Ingrediente.get('azúcar'), 20]
]

milkshake_Ingredientes = [
    [Ingrediente.get('leche'), 200],
    [Ingrediente.get('bola de helado'), 2],
    [Ingrediente.get('azúcar'), 15],
    [Ingrediente.get('fresas'), 100],
    [Ingrediente.get('azúcar'), 15]
]

smoothie_Ingredientes = [
    [Ingrediente.get('Moras azules'), 100],
    [Ingrediente.get('leche'), 150],
    [Ingrediente.get('azúcar'), 25],
    [Ingrediente.get('cubos de hielo'), 4]
]

cake = Producto('rebanada de pastel', 60 , cake_Ingredientes)
flan = Producto('rebanada de flan', 60, flan_Ingredientes)
brownie = Producto('brownie', 60 , brownie_Ingredientes)
cookies = Producto('docena de galletas', 60 , cookies_Ingredientes)
american = Producto('café americano', 60, amirican_Ingredientes)
milkshake = Producto('malteada de fresa', 60 , milkshake_Ingredientes)
smoothie = Producto('smoothie de mora azul', 60 , smoothie_Ingredientes)
