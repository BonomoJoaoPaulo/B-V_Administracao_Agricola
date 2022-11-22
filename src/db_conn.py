import os
import psycopg2, psycopg2.extras
import parameters

conn = None

def init_connection():
    global conn
    if conn is None:
        conn = psycopg2.connect(
            host = parameters.get_db_host(),
            user = parameters.get_db_user(),
            password = parameters.get_db_password(),
            port = parameters.get_db_port(),
            dbname = parameters.get_db_name(),
            cursor_factory = psycopg2.extras.DictCursor
        )

def close_connection():
    global conn
    if conn is not None:
        conn.close()
    conn = None

def get_connection():
    global conn
    if conn is None:
        init_connection()
    return conn