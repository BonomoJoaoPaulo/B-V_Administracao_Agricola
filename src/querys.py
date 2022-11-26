from db_conn import get_connection
from db_conn import close_connection


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
    

    return propertys_list

def get_property_cost(property_name):
    query = """SELECT p.ID_propriedade, rdc.* FROM Propriedade as p 
        JOIN Registro_custo_prop as rcp ON p.ID_propriedade = rcp.ID_propriedade
        JOIN Registro_de_Custo as rdc ON rcp.ID_registro_custo = rdc.ID_registro_custo
        WHERE p.nome = {property_name}"""

    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    cost_from_property_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            cost_from_property_list.append(value)

def get_property_workers(ID_propriedade):
    query = """ SELECT p.nome, f.* FROM Propriedade as p
        JOIN Funcionario as f ON p.ID_propriedade = f.ID_propriedade
        WHERE p.ID_propriedade = int{ID_propriedade}
    """

    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    property_workers_list = []

    for item in res:
        for value in item.values():
            value = str(value)
            property_workers_list.append(value)

def get_property_plantations(ID_propriedade):
    query = """ SELECT p.nome, c.nome, c.area_cultuvada FROM Propriedade as p
    JOIN Produz_prop_cult as ppc ON ppc.ID_propriedade = p.ID_propriedade
    JOIN Cultura as c ON ppc.ID_cultura = c.ID_cultura
    WHERE p.ID_propriedade = {ID_propriedade}
    """

    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    property_plantation = []

    for item in res:
        for value in item.value():
            value = str(value)
            property_plantation.append(value)

def get_culture_cost(ID_cultura):
    query = """ SELECT c.nome, c.area_cultivada, rdc.tipo_custo, rdc.descricao FROM Cultura as c
    JOIN Registro_custo_cult as rcc ON c.ID_cultura = rcc.ID_cultura
    JOIN Registro_de_custo as rdc ON rcc.ID_registro_custo = rdc.ID_registro_custo
    WHERE rdc.cultura_destinada = {ID_cultura}
    ORDER BY ASC
    """
    
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()

    culture_cost_ordered = []

    for item in res:
        for value in item.value():
            value = str(value)
            culture_cost_ordered.append(value)

