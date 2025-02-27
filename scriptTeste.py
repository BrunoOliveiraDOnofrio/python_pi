from datetime import timedelta
import threading
import mysql.connector
import time
import psutil
import keyboard

con = mysql.connector.connect(
            host="localhost",
            user="Python",
            passwd="py",
            database="opticar"
        )

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
def cpu():
    sql = 'SELECT valorDado, tipoDado, unidade FROM captura WHERE componente_id = "1"'
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql) 
    resultados = cursor.fetchall()  
    cursor.close()
    for linha in resultados:
        print("------------------------------------------------------------------")
        print("|                            CPU Máquina 3                       |")
        print("------------------------------------------------------------------")
        print("|                                                                |")
        print(f"| 1- {linha} |")
        print("|                                                                |")
        print("------------------------------------------------------------------")
    time.sleep(10)
    menu()



def ram():
    sql = 'SELECT valorDado, tipoDado, unidade FROM captura WHERE componente_id = "2"'
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql) 
    resultados = cursor.fetchall()  
    cursor.close()
    for linha in resultados:
        print("-----------------------------------------------------------------")
        print("|                          RAM Máquina 3                        |")
        print("-----------------------------------------------------------------")
        print("|                                                               |")
        print(f"| 1- {linha} |")
        print("|                                                               |")
        print("-----------------------------------------------------------------")
    time.sleep(10)
    menu()
def disco(escolha):
    if escolha == "1":
        sql = 'SELECT valorDado, tipoDado, unidade FROM captura WHERE tipoDado = "DISCO Tempo Leitura"'
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql) 
        resultados = cursor.fetchall()  
        cursor.close()
        for linha in resultados:
            print("-------------------------------------------------------------------------------")
            print("|                            DISCO Máquina 3 (Leitura)                        |")
            print("-------------------------------------------------------------------------------")
            print("|                                                                             |")
            print(f"| 1- {linha} |")
            print("|                                                                             |")
            print("-------------------------------------------------------------------------------")
        time.sleep(10)
        menu()
    elif escolha == "2":
        sql = 'SELECT valorDado, tipoDado, unidade FROM captura WHERE tipoDado = "DISCO Tempo Escrita"'
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql) 
        resultados = cursor.fetchall()  
        cursor.close()
        for linha in resultados:
            print("-------------------------------------------------------------------------------")
            print("|                            DISCO Máquina 3 (Escrita)                        |")
            print("-------------------------------------------------------------------------------")
            print("|                                                                             |")
            print(f"| 1- {linha} |")
            print("|                                                                             |")
            print("-------------------------------------------------------------------------------")
        time.sleep(10)
        menu()
def rede(escolha):
    if escolha == "1":
        sql = 'SELECT valorDado, tipoDado, unidade FROM captura WHERE tipoDado = "REDE Tempo Leitura"'
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql) 
        resultados = cursor.fetchall()  
        cursor.close()
        for linha in resultados:
            print("-------------------------------------------------------------------------------")
            print("|                            REDE Máquina 3 (Leitura)                        |")
            print("-------------------------------------------------------------------------------")
            print("|                                                                             |")
            print(f"| 1- {linha} |")
            print("|                                                                             |")
            print("-------------------------------------------------------------------------------")
        time.sleep(10)
        menu()
    elif escolha == "2":
        sql = 'SELECT valorDado, tipoDado, unidade FROM captura WHERE tipoDado = "REDE Tempo Escrita"'
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql) 
        resultados = cursor.fetchall()  
        cursor.close()
        for linha in resultados:
            print("--------------------------------------------------------------------------------")
            print("|                            REDE Máquina 3 (Escrita)                          |")
            print("--------------------------------------------------------------------------------")
            print("|                                                                              |")
            print(f"| 1- {linha} |")
            print("|                                                                              |")
            print("--------------------------------------------------------------------------------")
        time.sleep(10)
        menu()
def menu():
    # Menu
    print("-----------------------------------------------------------")
    print("|        Selecione um componente para visualizar          |")
    print("-----------------------------------------------------------")
    print("|                                                         |")
    print("|             1- CPU  2- RAM  3- DISCO  4- REDE           |")
    print("|                                                         |")
    print("-----------------------------------------------------------")
    escolha = input()

    if escolha == "1":
        cpu()
    elif escolha == "2":
        ram()
    elif escolha == "3":
        print("-----------------------------------------------------------")
        print("|              Selecione uma métrica para DISCO           |")
        print("-----------------------------------------------------------")
        print("|                                                         |")
        print("|                     1- Tempo Leitura                    |")
        print("|                     2- Tempo Escrita                    |")
        print("|                                                         |")
        print("-----------------------------------------------------------")
        escolha = input()
        if escolha == "1":
            disco(escolha)
        elif escolha == "2":
            disco(escolha)
    elif escolha == "4":
        print("-----------------------------------------------------------")
        print("|              Selecione uma métrica para REDE            |")
        print("-----------------------------------------------------------")
        print("|                                                         |")
        print("|                     1- Tempo Leitura                    |")
        print("|                     2- Tempo Escrita                    |")
        print("|                                                         |")
        print("-----------------------------------------------------------")
        escolha = input()
        if escolha == "1":
            rede(escolha)
        elif escolha == "2":
            rede(escolha)

menu()