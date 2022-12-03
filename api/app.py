from flask import Flask, jsonify, request
import psycopg2

from db_conn import get_connection
from db_conn import close_connection

app = Flask(__name__)

@app.route('/')
def working():
    return "It's working!"

@app.route('/Propriedade/read', methods=['GET'])
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

@app.route('/Propriedade/create', methods=['POST'])
def create_property():
    body = request.get_json()
    nome = body['nome']
    ultima_colheita_data = body['ultima_colheita_data']
    localidade = body['localidade']
    area_cultivada = body['area_cultivada']
    IDprodutor = body['IDprodutor']
    IDcultura = body['IDcultura']
    print(type(nome), type(ultima_colheita_data), type(area_cultivada), type(localidade), type(IDprodutor), type(IDcultura))
    query = f""" INSERT INTO Propriedade 
    (nome, area_cultivada, localidade, proprietário, cultura) VALUES
    ({body['nome']}, {body['ultima_colheita_data']}, {body['localidade']}, {body['area_cultivada']}, 
    {body['IDprodutor']}, {body['IDcultura']})"""

    with get_connection().cursor() as cursor:
        cursor.execute('INSERT INTO Propriedade (nome, ultima_colheita_data, localidade, area_cultivada, IDprodutor, IDcultura)'
            'VALUES (%s, %s, %s, %s, %s, %s)',
            (nome, ultima_colheita_data, localidade, area_cultivada, IDprodutor, IDcultura))
    close_connection()
    
    return "Property created"

# @app.route('/Propriedade/update', methods=['PUT'])
# def update_property():
#     body = request.get_json()
#     query = f""" UPDATE Propriedade SET
#     nome = {body['nome']}, ultima_colheita_data = {body['ultima_colheita_data']}, localidade = {body['localidade']}, area_cultivada = {body['area_cultivada']}, IDprodutor = {body['IDprodutor']}, IDcultura = {body['IDcultura']}
#     WHERE nome = {body['nome']}"""

#     with get_connection().cursor() as cursor:
#         cursor.execute(query)
#     close_connection()
    
#     return "Property updated"

@app.route('/Propriedade/delete', methods=['DELETE'])
def delete_property():
    body = request.get_json()
    query = f""" DELETE FROM Propriedade WHERE nome = {body['nome']}"""

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    close_connection()
    
    return "Property deleted"

if __name__ == '__main__':
    app.run(debug=True)