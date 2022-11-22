CREATE TABLE Propriedade 
( 
 nome INT,  
 ID_propriedade SERIAL PRIMARY KEY,  
 ultima_colheita_data DATE,  
 custo_ano FLOAT,  
 localidade VARCHAR(50),  
 faturamento_ano FLOAT,  
 proprietário INT,  
 cultura VARCHAR(50),  
 area_cultivada FLOAT,  
 ano INT
); 

CREATE TABLE Cultura 
( 
 ID_cultura SERIAL PRIMARY KEY ,  
 nome VARCHAR(50),  
 custo_ano FLOAT,  
 faturamento_ano FLOAT,  
 area_cultivada FLOAT,  
 ano INT
); 

CREATE TABLE Registro de Custo 
( 
 ID_registro_custo SERIAL PRIMARY KEY ,  
 tipo_custo VARCHAR(100),  
 valor_do_custo FLOAT,  
 local_de_despesa VARCHAR(50),  
 cultura_destinada VARCHAR(50),  
 propriedade_destino VARCHAR(50),  
 ano INT,  
 descrição VARCHAR(100) 
); 

CREATE TABLE Proprietário 
( 
 ID_proprietário SERIAL PRIMARY KEY ,  
 nome VARCHAR(100)
); 

CREATE TABLE Funcionário 
( 
 ID_funcionário SERIAL PRIMARY KEY ,  
 nome VARCHAR(50),  
 data_nascimento INT,  
 sexo CHAR(20),  
 telefone CHAR(15),  
 data_de_ingresso DATE,  
 salário FLOAT,  
 tipo VARCHAR(50)
); 

CREATE TABLE Maquinário 
( 
 ID_maquinário SERIAL PRIMARY KEY ,  
 custo_total FLOAT,  
 nome VARCHAR(100),  
 descrição VARCHAR(100)  
); 

CREATE TABLE Produz_prop_cult 
( 
 ID_prop_cult SERIAL PRIMARY KEY
); 

CREATE TABLE Registro_custo_cult 
( 
 ID_custo_cult SERIAL PRIMARY KEY
); 

CREATE TABLE Registro_custo_prop 
( 
 ID_custo_propri SERIAL PRIMARY KEY
); 

CREATE TABLE Rel_maquinário_cultura 
( 
 ID_maquinário_cultura SERIAL PRIMARY KEY
); 

CREATE TABLE Rel_maquinário_propriedade 
( 
 ID_rel_maquinário_propriedade SERIAL PRIMARY KEY 
); 

ALTER TABLE Propriedade ADD FOREIGN KEY(ID_proprietário) REFERENCES Proprietário (ID_proprietário)
ALTER TABLE Funcionário ADD FOREIGN KEY(ID_propriedade) REFERENCES Propriedade (ID_propriedade)
ALTER TABLE Funcionário ADD FOREIGN KEY(ID_proprietário) REFERENCES Proprietário (ID_proprietário)
ALTER TABLE Produz_prop_cult ADD FOREIGN KEY(ID_propriedade) REFERENCES Propriedade (ID_propriedade)
ALTER TABLE Produz_prop_cult ADD FOREIGN KEY(ID_cultura) REFERENCES Cultura (ID_cultura)
ALTER TABLE Registro_custo_cult ADD FOREIGN KEY(ID_cultura) REFERENCES Cultura (ID_cultura)
ALTER TABLE Registro_custo_cult ADD FOREIGN KEY(ID_registro_custo) REFERENCES Registro de Custo (ID_registro_custo)
ALTER TABLE Registro_custo_prop ADD FOREIGN KEY(ID_registro_custo) REFERENCES Registro de Custo (ID_registro_custo)
ALTER TABLE Registro_custo_prop ADD FOREIGN KEY(ID_propriedade) REFERENCES Propriedade (ID_propriedade)
ALTER TABLE Rel_maquinário_cultura ADD FOREIGN KEY(ID_cultura) REFERENCES Cultura (ID_cultura)
ALTER TABLE Rel_maquinário_cultura ADD FOREIGN KEY(ID_maquinário) REFERENCES Maquinário (ID_maquinário)
ALTER TABLE Rel_maquinário_propriedade ADD FOREIGN KEY(ID_maquinário) REFERENCES Maquinário (ID_maquinário)
ALTER TABLE Rel_maquinário_propriedade ADD FOREIGN KEY(ID_propriedade) REFERENCES Propriedade (ID_propriedade)