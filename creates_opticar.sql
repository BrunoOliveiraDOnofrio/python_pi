CREATE DATABASE opticar;

USE opticar;

CREATE TABLE empresa(
	id INT PRIMARY KEY AUTO_INCREMENT
    ,nome VARCHAR(90) NOT NULL
    ,cnpj VARCHAR(14) NOT NULL
    ,porte VARCHAR(7) NOT NULL
    ,fabricas INTEGER NOT NULL
    ,foto VARCHAR(255) NULL
    ,CONSTRAINT chkPorte CHECK (porte in('pequeno', 'medio', 'grande'))
);



CREATE TABLE usuario(
	id INT PRIMARY KEY AUTO_INCREMENT 
    ,nome VARCHAR(90) NOT NULL
    ,email VARCHAR(150) NOT NULL
    ,senha VARCHAR(35) NOT NULL
    ,cpf VARCHAR(11) NOT NULL
    ,cargo VARCHAR(45) NOT NULL
    ,nivel_permissao TINYINT DEFAULT 0
    ,foto VARCHAR(255) NULL 
    ,empresa_id INT NOT NULL
    ,data_admissao DATETIME NOT NULL
    ,CONSTRAINT chkNivelPermissao CHECK( nivel_permissao IN (0,1,2,3))
    ,CONSTRAINT fkEmpresaUsuario FOREIGN KEY (empresa_id) REFERENCES empresa(id)
);

CREATE TABLE logs(
	id INT PRIMARY KEY AUTO_INCREMENT 
    ,acao TEXT NOT NULL
    ,dataHora DATETIME NOT NULL
    ,usuario_id INT NULL
    ,CONSTRAINT fkUsuarioLogs FOREIGN KEY (usuario_id) REFERENCES usuario(id) 
);

CREATE TABLE alerta_config(
	id INT PRIMARY KEY AUTO_INCREMENT 
    ,tipoMetrica VARCHAR(20) NOT NULL
    ,limiteCritico FLOAT NOT NULL
    ,limiteAtencao FLOAT NOT NULL
    ,empresa_id INT NOT NULL
    ,CONSTRAINT fkEmpresaAlertaConfig FOREIGN KEY (empresa_id) REFERENCES empresa(id)
);

CREATE TABLE fabrica(
	id INT PRIMARY KEY AUTO_INCREMENT 
    ,logradouro VARCHAR(255) NOT NULL
    ,numLogradouro VARCHAR(6) NOT NULL
    ,uf CHAR(2) NOT NULL
    ,estado VARCHAR(25) NOT NULL
    ,cidade VARCHAR(90) NOT NULL
    ,bairro VARCHAR(90) NOT NULL
    ,complemento VARCHAR(100) NULL
    ,cep VARCHAR(8) NOT NULL
    ,servidores INTEGER NOT NULL
    ,empresa_id INT NOT NULL
    ,CONSTRAINT fkFabricaEmpresa FOREIGN KEY (empresa_id) REFERENCES empresa(id)
	
);

CREATE TABLE servidor(
	id INT PRIMARY KEY AUTO_INCREMENT 
    ,nome VARCHAR(40) NOT NULL
    ,descricao VARCHAR(255) NULL
    ,ipv4 VARCHAR(15) NOT NULL
    ,status_atual VARCHAR(20) NOT NULL DEFAULT ('Ativo')
    ,fabricante VARCHAR(50)
    ,sistema_operacional VARCHAR(50) NOT NULL 
    ,capacidade_ram FLOAT NOT NULL
    ,capacidade_disco FLOAT NOT NULL
    ,tipo_disco VARCHAR(10) NOT NULL
    ,data_instalacao DATETIME NOT NULL
    ,data_ultima_manutencao DATETIME NULL
    ,fabrica_id INT NOT NULL
    ,CONSTRAINT fkServidorFabrica FOREIGN KEY (fabrica_id) REFERENCES fabrica(id)
    ,CONSTRAINT chkStatusAtual CHECK (status_atual IN ('Ativo', 'Inativo', 'Manutenção'))
);

CREATE TABLE manutencao(
	id INT PRIMARY KEY AUTO_INCREMENT 
    ,descricao TEXT NOT NULL
    ,responsavel VARCHAR(80) NOT NULL
    ,dataHora DATETIME NOT NULL
    ,servidor_id INT NOT NULL
    ,CONSTRAINT fkServidorManutencao FOREIGN KEY (servidor_id) REFERENCES servidor(id)
);

CREATE TABLE intervalo_captura(
	id INT PRIMARY KEY AUTO_INCREMENT 
    ,cenario VARCHAR(40) NOT NULL
    ,intervalo INTEGER NOT NULL
    ,servidor_id INT NOT NULL
    ,CONSTRAINT fkIntervaloCapturaServidor FOREIGN KEY (servidor_id) REFERENCES servidor(id)
);

CREATE TABLE componente(
	id INT PRIMARY KEY AUTO_INCREMENT 
    ,tipo VARCHAR(45) NOT NULL 
    ,descricao VARCHAR(255) NULL
    ,modelo VARCHAR(70) NOT NULL
    ,fabricante VARCHAR(70) NOT NULL
    ,data_instalacao DATETIME NOT NULL
    ,servidor_id INT NOT NULL
    ,CONSTRAINT fkComponenteServidor FOREIGN KEY (servidor_id) REFERENCES servidor(id)
);

CREATE TABLE captura(
	id INT PRIMARY KEY AUTO_INCREMENT 
    ,valorDado FLOAT NOT NULL
    ,tipoDado VARCHAR(45)NOT NULL
    ,unidade VARCHAR(10) NOT NULL
    ,dataInicio DATETIME NOT NULL
    ,dataFinal DATETIME NOT NULL DEFAULT now()
    ,componente_id INT NOT NULL
    ,CONSTRAINT fkCapturaComponente FOREIGN KEY (componente_id) REFERENCES componente(id)
);

CREATE TABLE alerta(
	id INT PRIMARY KEY AUTO_INCREMENT 
    ,gravidade VARCHAR(20) NOT NULL
    ,descricao TEXT NOT NULL
    ,link_chamado VARCHAR(255) NOT NULL
    ,dataHora DATETIME NOT NULL	
    ,status VARCHAR(60)
    ,acaoTomada TEXT
    ,usuario_id INT NULL
    ,captura_id INT NOT NULL UNIQUE 
    ,CONSTRAINT fkAlertaUsuario FOREIGN KEY (usuario_id) REFERENCES usuario(id)
    ,CONSTRAINT fkAlertaCaptura FOREIGN KEY (captura_id) REFERENCES captura(id)
    ,CONSTRAINT chkStatus CHECK(status IN ('Aberto', 'Em Andamento', 'Fechado'))
);

CREATE TABLE processo(
	id INT PRIMARY KEY AUTO_INCREMENT 
    ,name VARCHAR(255) NOT NULL
    ,pid VARCHAR(50) NOT NULL
    ,status VARCHAR(10)
    ,alerta_id INT 
    ,CONSTRAINT fkProcessoAlerta FOREIGN KEY (alerta_id) REFERENCES alerta(id)
);







