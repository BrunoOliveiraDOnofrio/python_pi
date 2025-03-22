#!/bin/bash

echo "Atualizando a Biblioteca da VM (apt)";

sudo apt update;

echo "Biblioteca atualizada";

echo "Baixando Biblioteca apt";

sudo apt install -y;

echo "apt Baixado";

echo "Baixando o python3-pip";

sudo apt install -y python3-pip

echo "Python3-pip Baixado";

echo "Baixando o psutil";

pip3 install psutil --break-system-packages;

echo "psutil Baixado";

echo "Baixando o msql"

pip3 install mysql-connector-python --break-system-packages;

sudo apt install mysql-server -y

echo "msql Baixado"

echo "configurando o msql";

sudo systemctl start mysql;
sudo systemctl enable mysql;

echo "Servidor habilitado";

echo "Executando crate tables";

sudo mysql -u root -p"a" < /home/ubuntu/python_pi/creates_opticar.sql;

echo "Tabelas criadas";

echo "Executando inserts";

sudo mysql -u root -p"a" < /home/ubuntu/python_pi/inserts_opticar.sql;

echo "Inserts feito";

echo "Criando usuário";

sudo mysql -u root -p"a" < /home/ubuntu/python_pi/create_user.sql;

echo "Usuário criado e pronto para uso"

python3 App.py
