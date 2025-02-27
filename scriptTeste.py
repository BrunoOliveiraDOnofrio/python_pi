from datetime import timedelta
import threading
import mysql.connector
import time
import psutil
import keyboard

connection = mysql.connector.connect(
            host="10.18.33.33",
            user="usuario_inseridor",
            passwd="inseridor123",
            database="mydb"
        );

# Funcionalidades Requeridas
# Escolha da Máquina a ser Monitorada
# O usuário deve selecionar qual máquina deseja monitorar.

# Seleção do Componente a Ser Monitorado
# O usuário deve escolher um componente do sistema para monitorar (ex: CPU, Memória, Disco).

# Escolha da Métrica a Ser Acompanhada
# O usuário deve definir qual tipo de métrica será monitorada. As opções são:

# a) Percentual
# b) Bytes
# Tipo de Medida a Ser Apresentada
# O usuário pode escolher o tipo de medida que deseja visualizar. As opções são:

# a) Média por máquina (média dos valores de uso de cada máquina selecionada)
# b) Média total (média geral considerando todas as máquinas monitoradas)



# Requisitos Adicionais
# Continuidade ou Encerramento da Aplicação:
# Ao final de cada consulta, o usuário deve ser questionado se deseja continuar monitorando outra máquina/componente ou se deseja encerrar a aplicação.

# Organização da Informação:
# A informação apresentada ao usuário deve ser clara e bem estruturada, facilitando a leitura e compreensão. 

# Os requisitos listados não são limitativos. Sinta-se à vontade para utilizar a criatividade para adicionar funcionalidades extras ou melhorias na interface.
