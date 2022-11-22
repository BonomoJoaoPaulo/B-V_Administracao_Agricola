from db_conn import get_connection


db_conn = get_connection()
if (db_conn != None):
    print ("CONECTADO AO BANCO")