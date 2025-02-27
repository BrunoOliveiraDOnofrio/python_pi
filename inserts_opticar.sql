INSERT INTO empresa (nome, cnpj, porte, fabricas, foto) 
VALUES 
    ('AutoTech Indústria', '12345678000190', 'grande', 3, null),
    ('Mecânica Moderna', '98765432000110', 'medio', 2, null),
    ('Precisão Automotiva', '45678912000150', 'pequeno', 1, NULL);

INSERT INTO usuario (nome, email, senha, cpf, cargo, nivel_permissao, foto, empresa_id, data_admissao) 
VALUES 
    ('João Silva', 'joao.silva@autotech.com', 'senha123', '12345678901', 'Engenheiro de Manutenção', 2, null, 1, '2023-01-15 08:00:00'),
    ('Maria Oliveira', 'maria.oliveira@autotech.com', 'senha456', '98765432109', 'Analista de Dados', 1, NULL, 1, '2023-02-10 09:00:00'),
    ('Carlos Souza', 'carlos.souza@mecanica.com', 'senha789', '45678912345', 'Supervisor de Produção', 3, null, 2, '2023-03-20 10:00:00');
    
INSERT INTO logs (acao, dataHora, usuario_id) 
VALUES 
    ('Login realizado com sucesso', '2023-10-01 08:05:00', 1),
    ('Alerta crítico gerado para CPU', '2023-10-01 10:15:00', 2),
    ('Intervalo de captura alterado para 15 minutos', '2023-10-02 14:30:00', 3);
    
    INSERT INTO alerta_config (tipoMetrica, limiteCritico, limiteAtencao, empresa_id) 
VALUES 
    ('CPU', 90.0, 70.0, 1),
    ('RAM', 85.0, 65.0, 1),
    ('Disco', 80.0, 60.0, 2);
    
INSERT INTO fabrica (logradouro, numLogradouro, uf, estado, cidade, bairro, complemento, cep, servidores, empresa_id) 
VALUES 
    ('Rua das Indústrias', '100', 'SP', 'São Paulo', 'São Paulo', 'Centro', 'Prédio A', '01001000', 5, 1),
    ('Avenida das Máquinas', '200', 'RJ', 'Rio de Janeiro', 'Rio de Janeiro', 'Barra da Tijuca', NULL, '22010000', 3, 2),
    ('Travessa da Montagem', '300', 'MG', 'Minas Gerais', 'Belo Horizonte', 'Savassi', 'Galpão 10', '30120000', 2, 3);
    
INSERT INTO servidor (nome, descricao, ipv4, status_atual, fabricante, sistema_operacional, capacidade_ram, capacidade_disco, tipo_disco, data_instalacao, data_ultima_manutencao, fabrica_id) 
VALUES 
    ('Servidor SP-01', 'Servidor principal da fábrica de São Paulo', '192.168.1.1', 'Ativo', 'Dell', 'Windows Server 2022', 64.0, 1000.0, 'SSD', '2023-01-10 08:00:00', '2023-09-01 10:00:00', 1),
    ('Servidor RJ-01', 'Servidor de backup da fábrica do Rio de Janeiro', '192.168.2.1', 'Ativo', 'HP', 'Linux Ubuntu 22.04', 32.0, 2000.0, 'HDD', '2023-02-15 09:00:00', NULL, 2),
    ('Servidor BH-01', 'Servidor de monitoramento da fábrica de Belo Horizonte', '192.168.3.1', 'Manutenção', 'Lenovo', 'Windows Server 2019', 16.0, 500.0, 'SSD', '2023-03-20 10:00:00', '2023-08-25 14:00:00', 3);
 
INSERT INTO manutencao (descricao, responsavel, dataHora, servidor_id) 
VALUES 
    ('Substituição de disco rígido', 'João Silva', '2023-09-01 10:00:00', 1),
    ('Atualização do sistema operacional', 'Maria Oliveira', '2023-08-25 14:00:00', 3),
    ('Limpeza interna e troca de pasta térmica', 'Carlos Souza', '2023-07-15 11:30:00', 2);
    

INSERT INTO intervalo_captura (cenario, intervalo, servidor_id) 
VALUES 
    ('Crítico', 15, 1),
    ('Regular', 30, 1),
    ('Leve', 60, 1);
    
    INSERT INTO intervalo_captura (cenario, intervalo, servidor_id) 
VALUES 
    ('Crítico', 15, 2),
    ('Regular', 30, 2),
    ('Leve', 60, 2);
    
    
    INSERT INTO intervalo_captura (cenario, intervalo, servidor_id) 
VALUES 
    ('Crítico', 15, 3),
    ('Regular', 30, 3),
    ('Leve', 60, 3);
    
    
INSERT INTO componente (tipo, descricao, modelo, fabricante, data_instalacao, servidor_id) 
VALUES 
    ('CPU', 'Processador Intel Xeon', 'E5-2678', 'Intel', '2023-01-10 08:00:00', 3),
    ('RAM', 'Memória DDR4 16GB', 'DDR4-3200', 'Kingston', '2023-02-15 09:00:00', 3),
    ('Disco', 'SSD 500GB', '870 EVO', 'Samsung', '2023-03-20 10:00:00', 3);
    
INSERT INTO componente (tipo, descricao, modelo, fabricante, data_instalacao, servidor_id) 
VALUES 
    ('Placa de Rede', 'Placa de rede Gigabit Ethernet', 'EXPI9402PT', 'Intel', '2023-01-10 08:00:00', 3);
    