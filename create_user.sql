USE opticar;

CREATE USER 'usuario_inseridor'@'localhost' IDENTIFIED BY 'inseridor123';

GRANT ALL PRIVILEGES ON opticar.* TO 'usuario_inseridor'@'localhost';

FLUSH PRIVILEGES;
