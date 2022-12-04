from flask import Flask, jsonify, request
import psycopg2

from db_conn import get_connection
from db_conn import close_connection

app = Flask(__name__)

@app.route('/')
def working():
    return "It's working!"

@app.route('/Propriedade/create', methods=['POST'])
def create_property():
    body = request.get_json()
    nome = body['nome']
    ultima_colheita_data = body['ultima_colheita_data']
    localidade = body['localidade']
    area_cultivada = body['area_cultivada']
    IDprodutor = body['IDprodutor']
    IDcultura = body['IDcultura']

    query = (f"INSERT INTO Propriedade (nome) VALUES('{nome}', '{ultima_colheita_data}', '{localidade}', '{area_cultivada}', '{IDprodutor}', '{IDcultura}')")
    print(query)

    with get_connection().cursor() as cursor:
        cursor.execute(query)

    get_connection().commit()
    close_connection()
    
    return "Property created"

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

@app.route('/Propriedade/update', methods=['PUT'])
def update_property():
    body = request.get_json()
    id = body['id']
    new_name = body['name']
    query = (f"UPDATE Propriedade SET nome = ('{new_name}') WHERE ID_propriedade = ('{id}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "Property updated"

@app.route('/Propriedade/delete', methods=['DELETE'])
def delete_property():
    body = request.get_json()
    query = (f"DELETE FROM Propriedade WHERE ID_propriedade = ('{body['id']}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "Property deleted"


@app.route('/Cultura/create', methods=['POST'])
def create_culture():
    body = request.get_json()
    nome = body['nome']

    query = (f"INSERT INTO Cultura (nome) VALUES('{nome}')")
    print(query)

    with get_connection().cursor() as cursor:
        cursor.execute(query)

    get_connection().commit()
    close_connection()
    
    return "Culture created"

@app.route('/Cultura/read', methods=['GET'])
def get_all_cultures():
    query = """
        SELECT * FROM Cultura 
    """
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    cultures_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            cultures_list.append(value)
    
    return jsonify(res)

@app.route('/Cultura/update', methods=['POST'])
def update_culture():
    body = request.get_json()
    id = body['id']
    new_name = body['name']
    query = (f"UPDATE Cultura SET nome = ('{new_name}') WHERE ID_cultura = ('{id}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "Culture updated"

@app.route('/Cultura/delete', methods=['DELETE'])
def delete_culture():
    body = request.get_json()
    query = (f"DELETE FROM Cultura WHERE ID_cultura = ('{body['id']}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "Culture deleted"


@app.route('/Registro_de_Custo/create', methods=['POST'])
def create_cost_register():
    body = request.get_json()
    tipo_custo = body['tipo_custo']
    valor_do_custo = body['valor_do_custo']
    local_de_despesa = body['local_de_despesa']
    data = body['data']
    descricao_de_custo = body['descricao_de_custo']
    query = (f"INSERT INTO Registro_de_Custo (tipo_custo, valor_do_custo, local_de_despesa, data, descricao_de_custo) VALUES('{tipo_custo}', '{valor_do_custo}', '{local_de_despesa}', '{data}', '{descricao_de_custo}')")
    print(query)

    with get_connection().cursor() as cursor:
        cursor.execute(query)

    get_connection().commit()
    close_connection()
    
    return "Cost_Register created"

@app.route('/Registro_de_Custo/read', methods=['GET'])
def get_all_cost_register():
    query = """
        SELECT * FROM Registro_de_Custo 
    """
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    cost_registers_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            cost_registers_list.append(value)
    
    return jsonify(res)

@app.route('/Registro_de_Custo/update', methods=['POST'])
def update_cost_Register():
    body = request.get_json()
    id = body['id']
    new_value = body['value']
    query = (f"UPDATE Registro_de_Custo SET valor_do_custo = ('{new_value}') WHERE ID_registro_custo = ('{id}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "Cost_Register updated"

@app.route('/Registro_de_Custo/delete', methods=['DELETE'])
def delete_cost_Register():
    body = request.get_json()
    query = (f"DELETE FROM Registro_de_Custo WHERE ID_registro_custo = ('{body['id']}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "Cost_Register deleted"


@app.route('/Produtor/create', methods=['POST'])
def create_producer():
    body = request.get_json()
    nome = body['nome']

    query = (f"INSERT INTO Produtor (nome) VALUES('{nome}')")
    print(query)

    with get_connection().cursor() as cursor:
        cursor.execute(query)

    get_connection().commit()
    close_connection()
    
    return "producer created"

@app.route('/Produtor/read', methods=['GET'])
def get_all_producers():
    query = """
        SELECT * FROM Produtor 
    """
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    producers_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            producers_list.append(value)
    
    return jsonify(res)

@app.route('/Produtor/update', methods=['POST'])
def update_producer():
    body = request.get_json()
    id = body['id']
    new_name = body['name']
    query = (f"UPDATE Produtor SET nome = ('{new_name}') WHERE ID_produtor = ('{id}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "producer updated"

@app.route('/Produtor/delete', methods=['DELETE'])
def delete_producer():
    body = request.get_json()
    query = (f"DELETE FROM Produtor WHERE ID_produtor = ('{body['id']}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "producer deleted"


@app.route('/Funcionario/create', methods=['POST'])
def create_employee():
    body = request.get_json()
    nome = body['nome']
    data_nascimento = body['data_nascimento']
    sexo = body['sexo']
    telefone = body['telefone']
    data_de_ingresso = body['data_de_ingresso']
    salario = body['salario']
    tipo = body['tipo']
    idProdutor = body['idProdutor']
    idPropriedade = body['idPropriedade']
    
    query = (f"INSERT INTO Funcionario (nome, data_nascimento, sexo, telefone, data_de_ingresso, salario, tipo, idProdutor, idPropriedade) VALUES('{nome}', '{data_nascimento}', '{sexo}', '{telefone}', '{data_de_ingresso}', '{salario}', '{tipo}', '{idProdutor}', '{idPropriedade}')")
    print(query)

    with get_connection().cursor() as cursor:
        cursor.execute(query)

    get_connection().commit()
    close_connection()
    
    return "employee created"

@app.route('/Funcionario/read', methods=['GET'])
def get_all_employees():
    query = """
        SELECT * FROM Funcionario 
    """
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    employees_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            employees_list.append(value)
    
    return jsonify(res)

@app.route('/Funcionario/update', methods=['POST'])
def update_producer():
    body = request.get_json()
    id = body['id']
    new_name = body['name']
    query = (f"UPDATE Funcionario SET nome = ('{new_name}') WHERE ID_funcionario = ('{id}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "employee updated"

@app.route('/Funcionario/delete', methods=['DELETE'])
def delete_employee():
    body = request.get_json()
    query = (f"DELETE FROM Funcionario WHERE ID_funcionario = ('{body['id']}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "employee deleted"


@app.route('/Maquinario/create', methods=['POST'])
def create_machinery():
    body = request.get_json()
    nome = body['nome']
    descricao = body['descricao']
    query = (f"INSERT INTO Maquinario (nome, descricao) VALUES('{nome}', '{descricao}')")
    print(query)

    with get_connection().cursor() as cursor:
        cursor.execute(query)

    get_connection().commit()
    close_connection()
    
    return "machinery created"

@app.route('/Maquinario/read', methods=['GET'])
def get_all_machinerys():
    query = """
        SELECT * FROM Maquinario 
    """
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    machineries_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            machineries_list.append(value)
    
    return jsonify(res)

@app.route('/Maquinario/update', methods=['POST'])
def update_machinery():
    body = request.get_json()
    id = body['id']
    new_name = body['name']
    query = (f"UPDATE Maquinario SET nome = ('{new_name}') WHERE ID_maquinario = ('{id}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "machinery updated"

@app.route('/Maquinario/delete', methods=['DELETE'])
def delete_machinery():
    body = request.get_json()
    query = (f"DELETE FROM Maquinario WHERE ID_maquinario = ('{body['id']}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "machinery deleted"


@app.route('/Registro_custo_prop/create', methods=['POST'])
def create_cost_register_prop():
    body = request.get_json()
    ID_reg_custo_propriedade = body['ID_reg_custo_propriedade']
    ID_propriedade = body['ID_propriedade']

    query = (f"INSERT INTO Registro_custo_prop (ID_reg_custo_propriedade, ID_propriedade) VALUES('{ID_reg_custo_propriedade}', '{ID_propriedade}')")
    print(query)

    with get_connection().cursor() as cursor:
        cursor.execute(query)

    get_connection().commit()
    close_connection()
    
    return "cost_register_prop created"

@app.route('/Registro_custo_prop/read', methods=['GET'])
def get_all_cost_register_prop():
    query = """
        SELECT * FROM Registro_custo_prop
    """
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    cost_register_prop_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            cost_register_prop_list.append(value)
    
    return jsonify(res)

@app.route('/Registro_custo_prop/update', methods=['POST'])
def update_cost_register_prop():
    body = request.get_json()
    id = body['id']
    new_property = body['ID_propriedade']
    query = (f"UPDATE Registro_custo_prop SET ID_propriedade = ('{new_property}') WHERE ID_reg_custo_propriedade = ('{id}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "cost_register_prop updated"

@app.route('/Registro_custo_prop/delete', methods=['DELETE'])
def delete_cost_register_prop():
    body = request.get_json()
    query = (f"DELETE FROM Registro_custo_prop WHERE ID_reg_custo_propriedade = ('{body['id']}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "cost_register_prop deleted"


@app.route('/Rel_maquinario_cultura/create', methods=['POST'])
def create_rel_maq_cult():
    body = request.get_json()
    ID_cultura = body['ID_cultura']
    ID_maquinario = body['ID_maquinario']

    query = (f"INSERT INTO Rel_maquinario_cultura (ID_cultura, ID_maquinario) VALUES('{ID_cultura}', '{ID_maquinario}')")
    print(query)

    with get_connection().cursor() as cursor:
        cursor.execute(query)

    get_connection().commit()
    close_connection()
    
    return "rel_maq_cult created"

@app.route('/Rel_maquinario_cultura/read', methods=['GET'])
def get_all_rel_maq_cult():
    query = """
        SELECT * FROM Rel_maquinario_cultura
    """
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    rel_maq_cult_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            rel_maq_cult_list.append(value)
    
    return jsonify(res)

@app.route('/Rel_maquinario_cultura/update', methods=['POST'])
def update_rel_maq_cult():
    body = request.get_json()
    id = body['id']
    new_culture = body['ID_cultura']
    query = (f"UPDATE Rel_maquinario_cultura SET ID_cultura = ('{new_culture}') WHERE ID_maquinario_cultura = ('{id}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "rel_maq_cult updated"

@app.route('/Rel_maquinario_cultura/delete', methods=['DELETE'])
def delete_producer():
    body = request.get_json()
    query = (f"DELETE FROM Rel_maquinario_cultura WHERE ID_maquinario_cultura = ('{body['id']}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "rel_maq_cult deleted"


@app.route('/Rel_maquinario_propriedade/create', methods=['POST'])
def create_rel_maq_property():
    body = request.get_json()
    ID_propriedade = body['ID_propriedade']
    ID_maquinario = body['ID_maquinario']

    query = (f"INSERT INTO Rel_maquinario_propriedade (ID_propriedade, ID_maquinario) VALUES('{ID_propriedade}', '{ID_maquinario}')")
    print(query)

    with get_connection().cursor() as cursor:
        cursor.execute(query)

    get_connection().commit()
    close_connection()
    
    return "rel_maq_property created"

@app.route('/Rel_maquinario_propriedade/read', methods=['GET'])
def get_all_rel_maq_property():
    query = """
        SELECT * FROM Rel_maquinario_propriedade
    """
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    rel_maq_property_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            rel_maq_property_list.append(value)
    
    return jsonify(res)

@app.route('/Rel_maquinario_propriedade/update', methods=['POST'])
def update_rel_maq_cult():
    body = request.get_json()
    id = body['id']
    new_property = body['ID_propriedade']
    query = (f"UPDATE Rel_maquinario_propriedade SET ID_propriedade = ('{new_property}') WHERE ID_maquinario_propriedade = ('{id}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "rel_maq_property updated"

@app.route('/Rel_maquinario_propriedade/delete', methods=['DELETE'])
def delete_producer():
    body = request.get_json()
    query = (f"DELETE FROM Rel_maquinario_propriedade WHERE ID_maquinario_propriedade = ('{body['id']}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "rel_maq_property deleted"


@app.route('/Registro_custo_maquin/create', methods=['POST'])
def create_cost_register_maquin():
    body = request.get_json()
    ID_registro_custo_maquinario = body['ID_registro_custo_maquinario']
    ID_maquinario= body['ID_maquinario']

    query = (f"INSERT INTO Registro_custo_maquin (ID_registro_custo_maquinario, ID_maquinario) VALUES('{ID_registro_custo_maquinario}', '{ID_maquinario}')")
    print(query)

    with get_connection().cursor() as cursor:
        cursor.execute(query)

    get_connection().commit()
    close_connection()
    
    return "cost_register_maquin created"

@app.route('/Registro_custo_maquin/read', methods=['GET'])
def get_all_cost_register_maquin():
    query = """
        SELECT * FROM Registro_custo_maquin
    """
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    cost_register_maquin_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            cost_register_maquin_list.append(value)
    
    return jsonify(res)

@app.route('/Registro_custo_maquin/update', methods=['POST'])
def update_cost_register_prop():
    body = request.get_json()
    id = body['id']
    new_property = body['ID_maquinario']
    query = (f"UPDATE Registro_custo_maquin SET ID_maquinario = ('{new_property}') WHERE ID_registro_custo_maquinario = ('{id}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "cost_register_maquin updated"

@app.route('/Registro_custo_maquin/delete', methods=['DELETE'])
def delete_cost_register_prop():
    body = request.get_json()
    query = (f"DELETE FROM Registro_custo_maquin WHERE ID_registro_custo_maquinario = ('{body['id']}')")

    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()
    
    return "cost_register_maquin deleted"


if __name__ == '__main__':
    app.run(debug=True)