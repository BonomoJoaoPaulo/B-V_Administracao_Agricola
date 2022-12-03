CREATE TABLE Propriedade 
( 
ID_propriedade SERIAL PRIMARY KEY, 
nome VARCHAR(50), 
ultima_colheita_data DATE, 
localidade VARCHAR(50), 
area_cultivada FLOAT, 
idProdutor INT, 
idCultura INT, 
); 

CREATE TABLE Cultura 
( 
ID_cultura SERIAL PRIMARY KEY  , 
nome VARCHAR(50), 
); 

CREATE TABLE Registro de Custo 
( 
ID_registro_custo SERIAL PRIMARY KEY  , 
tipo_custo VARCHAR(50), 
valor_do_custo FLOAT, 
local_de_despesa VARCHAR(50), 
data DATE, 
descricao_de_custo VARCHAR(200), 
); 

CREATE TABLE Produtor 
( 
 ID_produtor SERIAL PRIMARY KEY  , 
nome VARCHAR(50), 
); 

CREATE TABLE Funcionario 
( 
ID_funcionario SERIAL PRIMARY KEY  , 
nome VARCHAR(50), 
data_nascimento DATE, 
sexo CHAR(1), 
telefone CHAR(11), 
data_de_ingresso DATE, 
salario FLOAT, 
tipo VARCHAR(50), 
idProdutor INT, 
idPropriedade INT, 
); 

CREATE TABLE Maquinario 
( 
ID_maquinario SERIAL PRIMARY KEY  , 
nome VARCHAR(50),
descricao VARCHAR(200),
); 

CREATE TABLE Registro_custo_prop 
( 
ID_reg_custo_propriedade SERIAL PRIMARY KEY  ,
ID_registro_custo INT, 
ID_propriedade INT, 
); 

CREATE TABLE Rel_maquinario_cultura 
( 
ID_maquinario_cultura SERIAL PRIMARY KEY  ,
ID_cultura INT, 
ID_maquinario INT, 
); 

CREATE TABLE Rel_maquinario_propriedade 
( 
ID_rel_maquinario_propriedade SERIAL PRIMARY KEY  ,
ID_maquinario INT, 
ID_propriedade INT, 
); 

CREATE TABLE Registro_custo_maquin 
( 
ID_registro_custo_maquinario SERIAL PRIMARY KEY  ,
ID_registro_custo INT, 
ID_maquinario INT, 
); 

ALTER TABLE Propriedade ADD FOREIGN KEY(idProdutor) REFERENCES Produtor (idProdutor)
ALTER TABLE Propriedade ADD FOREIGN KEY(idCultura) REFERENCES Cultura (idCultura)
ALTER TABLE Funcionario ADD FOREIGN KEY(idProdutor) REFERENCES Produtor (idProdutor)
ALTER TABLE Funcionario ADD FOREIGN KEY(idPropriedade) REFERENCES Propriedade (idPropriedade)
ALTER TABLE Registro_custo_prop ADD FOREIGN KEY(ID_registro_custo) REFERENCES Registro de Custo (ID_registro_custo)
ALTER TABLE Registro_custo_prop ADD FOREIGN KEY(ID_propriedade) REFERENCES Propriedade (ID_propriedade)
ALTER TABLE Rel_maquinario_cultura ADD FOREIGN KEY(ID_cultura) REFERENCES Cultura (ID_cultura)
ALTER TABLE Rel_maquinario_cultura ADD FOREIGN KEY(ID_maquinario) REFERENCES Maquinario (ID_maquinario)
ALTER TABLE Rel_maquinario_propriedade ADD FOREIGN KEY(ID_maquinario) REFERENCES Maquinario (ID_maquinario)
ALTER TABLE Rel_maquinario_propriedade ADD FOREIGN KEY(ID_propriedade) REFERENCES Propriedade (ID_propriedade)
ALTER TABLE Registro_custo_maquin ADD FOREIGN KEY(ID_registro_custo) REFERENCES Registro de Custo (ID_registro_custo)
ALTER TABLE Registro_custo_maquin ADD FOREIGN KEY(ID_maquinario) REFERENCES Maquinario (ID_maquinario)

