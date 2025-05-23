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
    def select_all_pedidos() -> list:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = 'SELECT * FROM cafeteria.pedidos'  
        
        try:
            cursor.execute( query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            key.close()
            
       
    @staticmethod
    def productos_pedidos() -> list:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = '''SELECT id, pastel, flan , docena_galletas, brownie, americano, malteada, smoothie
        FROM cafeteria.pedidos WHERE entregado = False ORDER BY id 
        '''
        
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
        query = '''SELECT id, pastel, flan , docena_galletas, brownie, americano, malteada, smoothie,fecha, total
        FROM cafeteria.pedidos WHERE entregado = True
        '''
        
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            return f'Error: {e}'
        finally:
            cursor.close()
            key.close()
     
    @staticmethod       
    def ventas_dia_actual()-> list:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = '''
        SELECT id, pastel, flan, docena_galletas, brownie, americano, malteada, smoothie, fecha, total
        FROM cafeteria.pedidos
        WHERE entregado = True
        AND DATE(fecha) = CURDATE()
        '''
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            key.close()
            
    @staticmethod
    def ventas_semana_actual()-> list:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = '''
        SELECT id, pastel, flan, docena_galletas, brownie, americano, malteada, smoothie, fecha, total
        FROM cafeteria.pedidos
        WHERE entregado = True
        AND YEARWEEK(fecha, 1) = YEARWEEK(CURDATE(), 1)
        '''
        
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e :
            print(f'Error: {e}')
        finally:
            cursor.close()
            key.close()
            
    @staticmethod
    def ventas_mes_actual()->list:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = '''
        SELECT id, pastel, flan, docena_galletas, brownie, americano, malteada, smoothie, fecha, total
        FROM cafeteria.pedidos
        WHERE entregado = True
        AND MONTH(fecha) = MONTH(CURDATE())
        AND YEAR(fecha) = YEAR(CURDATE())
        '''
        
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            key.close()
            
    @staticmethod
    def ventas_año_actual()->list:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = '''
        SELECT id, pastel, flan, docena_galletas, brownie, americano, malteada, smoothie, fecha, total
        FROM cafeteria.pedidos
        WHERE entregado = True
        AND YEAR(fecha) = YEAR(CURDATE())
        '''
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f'Error: {e}')
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

    @staticmethod
    def top_productos():
        conexion = Connection.connectBD()
        cursor = conexion.cursor()
        query = """
            SELECT 'PASTEL', SUM(pastel) FROM pedidos WHERE entregado = True
            UNION
            SELECT 'FLAN', SUM(flan) FROM pedidos WHERE entregado = True
            UNION
            SELECT 'GALLETAS', SUM(docena_galletas) FROM pedidos WHERE entregado = True
            UNION
            SELECT 'BROWNIE', SUM(brownie) FROM pedidos WHERE entregado = True
            UNION
            SELECT 'AMERICANO', SUM(americano) FROM pedidos WHERE entregado = True
            UNION
            SELECT 'MALTEADA', SUM(malteada) FROM pedidos WHERE entregado = True
            UNION
            SELECT 'SMOOTHIE', SUM(smoothie) FROM pedidos WHERE entregado = True
        """
        try:
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            cursor.close()
            conexion.close()
            
    @staticmethod
    def sum_hoy() -> int:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = '''SELECT SUM(total) FROM cafeteria.pedidos
        WHERE entregado = True
        AND DATE(fecha) = CURDATE()'''
        
        try:
            cursor.execute(query)
            tot = cursor.fetchone()
            return tot[0] if tot[0] is not None else 0
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            key.close()
       
    @staticmethod     
    def sum_semana()-> int:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = '''
        SELECT SUM(total)
        FROM cafeteria.pedidos
        WHERE entregado = True
        AND YEARWEEK(fecha, 1) = YEARWEEK(CURDATE(), 1)
        '''
        
        try:
            cursor.execute(query)
            tot = cursor.fetchone()
            return tot[0] if tot[0] is not None else 0
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            key.close()
            
    @staticmethod
    def sum_mes()-> int:
        key = Connection.connectBD()
        cursor = key.cursor()
        query = '''
        SELECT SUM(total)
        FROM cafeteria.pedidos
        WHERE entregado = True
        AND MONTH(fecha) = MONTH(CURDATE())
        AND YEAR(fecha) = YEAR(CURDATE())
        '''
        try:
            cursor.execute(query)
            tot = cursor.fetchone()
            return tot[0] if tot[0] is not None else 0
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            key.close()
            
    @staticmethod
    def sum_año()-> int :
        key = Connection.connectBD()
        cursor = key.cursor()
        query = '''
        SELECT SUM(total)
        FROM cafeteria.pedidos
        WHERE entregado = True
        AND YEAR(fecha) = YEAR(CURDATE())
        '''
        try:
            cursor.execute(query)
            tot = cursor.fetchone()
            return tot[0] if tot[0] is not None else 0
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            key.close()
            
    @staticmethod
    def sum_total()-> int :
        key = Connection.connectBD()
        cursor = key.cursor()
        query = 'SELECT SUM(total) from cafeteria.pedidos'
        
        try:
            cursor.execute(query)
            tot = cursor.fetchone()
            return tot[0] if tot[0] is not None else 0
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            cursor.close()
            key.close()
