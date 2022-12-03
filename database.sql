CREATE TABLE Propriedade 
( 
 ID_propriedade INT PRIMARY KEY AUTO_INCREMENT,
 nome VARCHAR(n),  
 ultima_colheita_data DATE,  
 localidade VARCHAR(n),  
 area_cultivada FLOAT,  
 idProdutor INT,  
 idCultura INT,  
); 

CREATE TABLE Cultura 
( 
 ID_cultura INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(n),  
); 

CREATE TABLE Registro de Custo 
( 
 ID_registro_custo INT PRIMARY KEY AUTO_INCREMENT,  
 tipo_custo VARCHAR(n),  
 valor_do_custo FLOAT,  
 local_de_despesa VARCHAR(n),  
 data DATE,  
 descricao_de_custo VARCHAR(n),  
); 

CREATE TABLE Produtor 
( 
 ID_produtor INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(n),  
); 

CREATE TABLE Funcionario 
( 
 ID_funcionario INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(n),  
 data_nascimento DATE,  
 sexo CHAR(n),  
 telefone CHAR(n),  
 data_de_ingresso DATE,  
 salario FLOAT,  
 tipo VARCHAR(n),  
 idProdutor INT,  
 idPropriedade INT,  
); 

CREATE TABLE Maquinario 
( 
 ID_maquinario INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(n),  
 descricao VARCHAR(n),  
); 

CREATE TABLE Registro_custo_prop 
( 
 ID_reg_custo_propriedade INT PRIMARY KEY AUTO_INCREMENT,  
 ID_registro_custo INT,  
 ID_propriedade INT,  
); 

CREATE TABLE Rel_maquinario_cultura 
( 
 ID_maquinario_cultura INT PRIMARY KEY AUTO_INCREMENT,  
 ID_cultura INT,  
 ID_maquinario INT,  
); 

CREATE TABLE Rel_maquinario_propriedade 
( 
 ID_rel_maquinario_propriedade INT PRIMARY KEY AUTO_INCREMENT,  
 ID_maquinario INT,  
 ID_propriedade INT,  
); 

CREATE TABLE Registro_custo_maquin 
( 
 ID_registro_custo_maquinario INT PRIMARY KEY AUTO_INCREMENT,  
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
