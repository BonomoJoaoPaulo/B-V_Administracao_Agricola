from flask import Flask, jsonify, request
import psycopg2

from db_conn import get_connection
from db_conn import close_connection

app = Flask(__name__)

@app.route('/')
def working():
    return "It's working!"

@app.route('/propriedades/read', methods=['GET'])
def get_all_propertys():
    query = """
        SELECT nome FROM Propriedade 
    """
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    propertys_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            propertys_list.append(value)
    

    return jsonify(propertys_list)

@app.route('/propriedades/create', methods=['POST'])
def create_property():
    body = request.get_json()
    query = f""" INSERT INTO Propriedade 
    (nome, area, endereco, telefone, email, ID_proprietario) VALUES
    ({body['nome']}, {body['area']}, {body['endereco']}, {body['telefone']}, {body['email']}, {body['ID_proprietario']})"""

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    close_connection()
    
    return "Property created"

@app.route('/propriedades/update', methods=['PUT'])
def update_property():
    body = request.get_json()
    query = f""" UPDATE Propriedade SET
    nome = {body['nome']}, area = {body['area']}, endereco = {body['endereco']}, telefone = {body['telefone']}, email = {body['email']}, ID_proprietario = {body['ID_proprietario']}
    WHERE nome = {body['nome']}"""

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    close_connection()
    
    return "Property updated"

@app.route('/propriedades/delete', methods=['DELETE'])
def delete_property():
    body = request.get_json()
    query = f""" DELETE FROM Propriedade WHERE nome = {body['nome']}"""

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    close_connection()
    
    return "Property deleted"

if __name__ == '__main__':
    app.run(debug=True)