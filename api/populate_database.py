import psycopg2
from db_conn import get_connection
from db_conn import close_connection

def create_tables():
    sql = '''CREATE TABLE Propriedade( 
    ID_propriedade SERIAL PRIMARY KEY, 
    nome VARCHAR(50), 
    ultima_colheita_data DATE, 
    localidade VARCHAR(50), 
    area_cultivada FLOAT, 
    idProdutor INT, 
    idCultura INT
    )'''
    with get_connection().cursor() as cursor:		
            cursor.execute(sql)
    close_connection()


if __name__ == '__main__':
	create_tables()
