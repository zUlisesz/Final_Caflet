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
