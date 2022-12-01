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
        SELECT * FROM Propriedade 
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
    
    return jsonify(res)

@app.route('/propriedades/create', methods=['POST'])
def create_property():
    body = request.get_json()
    nome = body['nome']
    area_cultivada = body['area_cultivada']
    localidade = body['localidade']
    proprietario = body['proprietário']
    cultura = body['cultura']
    print(type(nome), type(area_cultivada), type(localidade), type(proprietario), type(cultura))
    query = f""" INSERT INTO Propriedade 
    (nome, area_cultivada, localidade, proprietário, cultura) VALUES
    ({body['nome']}, {body['area_cultivada']}, {body['localidade']}, {body['proprietário']}, {body['cultura']})"""

    with get_connection().cursor() as cursor:
        cursor.execute('INSERT INTO Propriedade (nome, area_cultivada, localidade, proprietário, cultura)'
            'VALUES (%s, %s, %s, %s, %s)',
            (10, area_cultivada, localidade, 1, cultura))
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