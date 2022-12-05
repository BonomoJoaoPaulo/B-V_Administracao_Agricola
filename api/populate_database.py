import psycopg2
from db_conn import get_connection
from db_conn import close_connection

def populate_database():
    #sql = "INSERT INTO Cultura (nome) VALUES('arroz'),('milho'),('soja')"
    #sql = "INSERT INTO Produtor (nome) VALUES('Antonio'), ('Joao'), ('Pedro')"
    #sql = "INSERT INTO Propriedade (nome, ultima_colheita_data, localidade, area_cultivada, idProdutor, idCultura) VALUES('Fazenda1', '10-10-2020', 'Orleans', '20', '1', '5'), ('Fazenda2', '2-22-2021', 'Sao Mateus', '50', '3', '2'), ('Fazenda3', '3-2-2022', 'Tres Barras', '100', '3', '6')"
    #sql = "INSERT INTO Maquinario (nome, descricao) VALUES('Trator', 'Masseyferguson'), ('Colheitadeira', 'NewHolland'), ('Plantadeira', 'JohnDeere')"
    #sql = "INSERT INTO Funcionario (nome, data_nascimento, sexo, telefone, data_de_ingresso, salario, tipo, idProdutor, idPropriedade) VALUES ('Jose', '10-10-1990', 'M', '999999999', '10-10-2020', '1000', 'Gerente', '1', '1'), ('Josafat', '10-10-1990', 'M', '999999998', '10-10-2020', '1000', 'Mecanico', '2', '2'), ('Jozimar', '10-10-1990', 'M', '999999997', '10-10-2020', '1000', 'Gerente', '3', '3')"
    #sql = "INSERT INTO Registro_de_Custo (tipo_custo, valor_do_custo, local_de_despesa, data, descricao_de_custo) VALUES ('Fertilizante', '552.6', 'Agropecuaria Volpato', '10-10-2020', 'Fertilizante para plantio'), ('Fertilizante', '552.6', 'Agropecuaria Volpato', '10-10-2020', 'Fertilizante para plantio'), 
    # ('Espingardinha', '2000', 'Agropecuaria Volpato', '10-10-2021', 'Espingarda para controle de pragas'), ('Ureia', '360', 'Agropecuaria Volpato', '1-5-2020', 'Ureia para o solo'), ('Randap', '150', 'Agropecuaria Volpato', '12-5-2020', 'Randap para matar erva daninha'), 
    # ('Defensivo agricola', '5000', 'Agropecuaria Volpato', '1-5-2009', 'Controle de larvas'), ('Bota', '50', 'Agropecuaria Volpato', '5-12-2021', 'Bota para funcionário'), ('Cerveja', '500', 'Supermercado Volpato', '12-12-2021', 'Confraternizaçao fim de ano')"
    #sql = "INSERT INTO Rel_Maquinario_Propriedade (ID_maquinario, ID_propriedade) VALUES ('1', '1'), ('2', '1'), ('3', '1')"
    #sql = "INSERT INTO Rel_Maquinario_Cultura (ID_maquinario, ID_cultura) VALUES ('1', '5'), ('2', '5'), ('3', '5')"
    #sql = "INSERT INTO Registro_custo_prop (ID_registro_custo, ID_propriedade) VALUES ('1', '1'), ('2', '1'), ('3', '1'), ('4', '1'), ('5', '1'), ('6', '1'), ('7', '1'), ('8', '1')"

    #sql = """INSERT INTO Registro_de_Custo (tipo_custo, valor_do_custo, local_de_despesa, data, descricao_de_custo) VALUES ('Fertilizante', '582.6', 'Agropecuaria Volpato', '10-10-2020', 'Fertilizante para plantio'), ('Fertilizante', '960.6', 'Agropecuaria Volpato', '10-10-2020', 'Fertilizante para plantio'), 
    #('Espingardinha', '3000', 'Agropecuaria Volpato', '10-10-2021', 'Espingarda para controle de pragas'), ('Ureia', '30000', 'Agropecuaria Volpato', '1-5-2020', 'Ureia para o solo'), ('Randap', '150', 'Agropecuaria Volpato', '12-5-2020', 'Randap para matar erva daninha'), 
    #('Defensivo agricola', '500', 'Agropecuaria Volpato', '1-5-2009', 'Controle de larvas'), ('Bota', '50', 'Agropecuaria Volpato', '5-12-2021', 'Bota para funcionário'), ('Penetone', '500', 'Supermercado Volpato', '12-12-2021', 'Confraternizaçao fim de ano')"""
    #sql = "INSERT INTO Registro_custo_prop (ID_registro_custo, ID_propriedade) VALUES ('9', '2'), ('10', '2'), ('11', '2'), ('12', '2'), ('13', '2'), ('14', '2'), ('15', '2'), ('16', '2')"
    # sql = """INSERT INTO Funcionario (nome, data_nascimento, sexo, telefone, data_de_ingresso, salario, tipo, idProdutor, idPropriedade) VALUES ('Rafael', '10-10-2003', 'M', '999999993', '10-10-2020', '500', 'Boia-Fria', '1', '1'), ('Gustavo', '10-10-1997', 'M', '999999991', '10-10-2020', '10000', 'Agronomo', '2', '2'), ('Alemao', '10-10-2002', 'M', '999999992', '10-10-2020', '1000', 'Tratoreiro', '3', '3'),
    # ('Matheus', '10-10-1999', 'M', '998999993', '10-10-2020', '990', 'OpeMaquinario', '1', '1'), ('Leonardo', '10-10-1998', 'M', '999979991', '10-10-2020', '10000', 'Caseiro', '2', '2'), ('Ze', '10-10-2002', 'M', '999699992', '10-10-2020', '1000', 'Supervisor', '3', '3')"""

    #sql = """INSERT INTO Registro_de_Custo (tipo_custo, valor_do_custo, local_de_despesa, data, descricao_de_custo) VALUES ('Gasolina', '5890', 'Posto Volpato', '10-10-2010', 'Gasolina maq'), ('Disel', '9154', 'Posto Volpato', '10-10-2011', 'Disel para maqnario'),
    #('Gasolina', '5901', 'Posto Volpato', '10-10-2019', 'Gasolina maq'), ('Disel', '9604', 'Posto Volpato', '10-10-2019', 'Disel para maqnario'), ('sementes', '16000', 'Agropecuaria Volpato', '10-10-2018', 'sementes'), ('Adubo', '9040', 'Agropecuaria Volpato', '10-10-2018', 'Adubo')"""
    #sql = "INSERT INTO Registro_custo_prop (ID_registro_custo, ID_propriedade) VALUES ('17', '1'), ('18', '1'), ('19', '1'), ('20', '1'), ('21', '1'), ('22', '1'), ('23', '1'), ('24', '1')"
    
    sql = "INSERT INTO Funcionario (nome, data_nascimento, sexo, telefone, data_de_ingresso, salario, tipo, idProdutor, idPropriedade) VALUES ('Juliane', '10-10-1997', 'F', '999799999', '10-07-2021', '1100', 'Secretaria', '1', '1'), ('Emerson', '04-02-1978', 'M', '999699998', '05-10-2020', '1200', 'Mecanico', '1', '1'), ('Rodrigo', '10-10-1983', 'M', '999999997', '10-10-2019', '1500', 'Tratorista', '3', '3'), ('Baloti', '10-10-1983', 'M', '999999991', '09-10-2009', '1100', 'Funcionario rural', '2', '2'), ('Hugo', '11-08-1992', 'M', '999939991', '08-03-2020', '8000', 'Agronomo', '1', '1'), ('Anderson', '08-01-1998', 'M', '999933991', '08-03-2021', '1100', 'Funcionario rural', '2', '2')"
    
    sql = "INSERT INTO Registro_de_Custo (tipo_custo, valor_do_custo, local_de_despesa, data, descricao_de_custo) VALUES ('Cerveja e carne', '249.9', 'Supermercado Volpato', '12-12-2011', 'Confraternizaçao fim de ano'), ('Fertilizante', '5820.6', 'Agropecuaria Volpato', '10-10-2012', 'Fertilizante para plantio'), ('Fertilizante', '9600.6', 'Agropecuaria Volpato', '10-10-2013', 'Fertilizante para plantio'), ('Fertilizante', '3670.5', 'Agropecuaria Volpato', '10-10-2014', 'Fertilizante para plantio'), ('Ureia', '30000', 'Agropecuaria Volpato', '1-5-2015', 'Ureia para o solo'), ('Cerveja e carne', '549.9', 'Supermercado Volpato', '12-12-2016', 'Confraternizaçao fim de ano'), ('Cerveja e carne', '499.9', 'Supermercado Volpato', '12-12-2017', 'Confraternizaçao fim de ano'), ('Randap', '1509', 'Agropecuaria Volpato', '12-5-2018', 'Randap para matar erva daninha'), ('Defensivo agricola', '5007.1', 'Agropecuaria Volpato', '1-5-2019', 'Controle de larvas'), ('Bota', '200', 'Agropecuaria Volpato', '5-09-2011', 'Bota para funcionário'), ('Cerveja', '500', 'Supermercado Volpato', '12-12-2021', 'Confraternizaçao fim de ano'), ('Mangueiras e gotejadores', '1000', 'Sacconi Irrigação', '03-12-2020', 'Irrigação da nova propriedade')"

    sql = "INSERT INTO Registro_custo_prop ('25', '1'), ('26', '1'), ('27', '3'), ('28', '2'), ('29', '3'), ('30', '1'), ('31', '2'), ('32', '2'), ('33', '3'), ('34', '1'), ('35', '3')"


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
