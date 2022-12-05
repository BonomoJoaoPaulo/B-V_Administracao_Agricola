import psycopg2
from db_conn import get_connection
from db_conn import close_connection

def populate_database():
    #sql = "INSERT INTO Cultura (nome) VALUES('arroz'),('milho'),('soja')"
    #sql = "INSERT INTO Propriedade (nome, ultima_colheita_data, localidade, area_cultivada, idProdutor, idCultura) VALUES('Fazenda1', '10-10-2020', 'Orleans', '20', '1', '5'), ('Fazenda2', '2-22-2021', 'Sao Mateus', '50', '3', '2'), ('Fazenda3', '3-2-2022', 'Tres Barras', '100', '3', '6')"
    #sql = "INSERT INTO Produtor (nome) VALUES('Antonio'), ('Joao'), ('Pedro')"
    #sql = "INSERT INTO Maquinario (nome, descricao) VALUES('Trator', 'Masseyferguson'), ('Colheitadeira', 'NewHolland'), ('Plantadeira', 'JohnDeere')"
    #sql = "INSERT INTO Funcionario (nome, data_nascimento, sexo, telefone, data_de_ingresso, salario, tipo, idProdutor, idPropriedade) VALUES ('Jose', '10-10-1990', 'M', '999999999', '10-10-2020', '1000', 'Gerente', '1', '1'), ('Josafat', '10-10-1990', 'M', '999999998', '10-10-2020', '1000', 'Mecanico', '2', '2'), ('Jozimar', '10-10-1990', 'M', '999999997', '10-10-2020', '1000', 'Gerente', '3', '3')"
    #sql = "INSERT INTO Registro_de_Custo (tipo_custo, valor_do_custo, local_de_despesa, data, descricao_de_custo) VALUES ('Fertilizante', '552.6', 'Agropecuaria Volpato', '10-10-2020', 'Fertilizante para plantio'), ('Fertilizante', '552.6', 'Agropecuaria Volpato', '10-10-2020', 'Fertilizante para plantio'), 
    # ('Espingardinha', '2000', 'Agropecuaria Volpato', '10-10-2021', 'Espingarda para controle de pragas'), ('Ureia', '360', 'Agropecuaria Volpato', '1-5-2020', 'Ureia para o solo'), ('Randap', '150', 'Agropecuaria Volpato', '12-5-2020', 'Randap para matar erva daninha'), 
    # ('Defensivo agricola', '5000', 'Agropecuaria Volpato', '1-5-2009', 'Controle de larvas'), ('Bota', '50', 'Agropecuaria Volpato', '5-12-2021', 'Bota para funcionário'), ('Cerveja', '500', 'Supermercado Volpato', '12-12-2021', 'Confraternizaçao fim de ano')"
    #sql = "INSERT INTO Rel_Maquinario_Propriedade (ID_maquinario, ID_propriedade) VALUES ('1', '1'), ('2', '1'), ('3', '1')"
    #sql = "INSERT INTO Rel_Maquinario_Cultura (ID_maquinario, ID_cultura) VALUES ('1', '5'), ('2', '5'), ('3', '5')"
    #sql = "INSERT INTO Registro_custo_prop (ID_registro_custo, ID_propriedade) VALUES ('1', '1'), ('2', '1'), ('3', '1'), ('4', '1'), ('5', '1'), ('6', '1'), ('7', '1'), ('8', '1')"

    with get_connection().cursor() as cursor:		
            cursor.execute(sql)
    get_connection().commit()
    close_connection()


def consulte_database():
    sql = "SELECT * FROM Registro_de_Custo"
    with get_connection().cursor() as cursor:		
            cursor.execute(sql)
            result = cursor.fetchall()
    get_connection().commit()
    close_connection()
    return result


if __name__ == '__main__':
	populate_database()
