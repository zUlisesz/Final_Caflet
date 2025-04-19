from database.conex import Connection
import mysql.connector
class Consulta:
    
    @staticmethod
    def all_ingredientes()->list:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = 'SELECT * FROM cafeteria.ingredientes'
        
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e :
            return f'Error: {e}'
        finally:
            cursor.close()
            key.close
            
    @staticmethod
    def all_pedidos() -> list:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = 'SELECT * FROM cafeteria.pedidos WHERE entregado = False;'
        
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            return f'Error: {e}'
        finally:
            cursor.close()
            key.close()
            
    @staticmethod
    def all_ventas() -> list:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = 'SELECT * FROM cafeteria.pedidos WHERE entregado = True;'
        
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            return f'Error: {e}'
        finally:
            cursor.close()
            key.close()
            
    @staticmethod
    def set_entregado(id) -> None:
        key = Connection.connectBD()
        cursor = key.cursor()    
        query = 'UPDATE cafeteria.pedidos SET entregado = True WHERE id = %s; '
        
        try:
            cursor.execute(query,(id,))
            key.commit()
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close() 
            key.close()
            
    @staticmethod
    def update_ingredientes(nombre , cantidad) ->None:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = 'UPDATE cafeteria.ingredientes SET cantidad = %s WHERE nombre = %s;'
        
        try:
            cursor.execute( query, (cantidad, nombre))
            key.commit()
        except mysql.connector.Error as e:
            print(f'Error al actualizar: {e}')
        finally:
            cursor.close()
            key.close()
            
    @staticmethod
    def send_pedido(orden) -> None:
        key = Connection.connectBD()
        cursor = key.cursor() 
        query = '''
        INSERT INTO cafeteria.pedidos(
        pastel, flan, docena_galletas, brownie, americano, malteada, smoothie, fecha, total, entregado) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        
        values = tuple(orden.preparar_envio())
        
        try:
            cursor.execute(query, values)
            key.commit()
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            key.close()

