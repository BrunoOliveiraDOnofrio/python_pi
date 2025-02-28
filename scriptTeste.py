from datetime import timedelta
import threading
import mysql.connector
import time
import psutil
import keyboard

con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="linkinpark",
            database="opticar"
)

# Funcionalidades Requeridas
# Escolha da Máquina a ser Monitorada
# O usuário deve selecionar qual máquina deseja monitorar.
senha = "123"
def definir_maquina():
    
    rep = True
    sql = 'SELECT id, nome FROM servidor'
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql) 
    resultados = cursor.fetchall()  
    cursor.close()
    while rep:
        for linha in resultados:
            print("-----------------------------------------------------------")
            print("|                   Selecione uma máquina                 |")
            print("-----------------------------------------------------------")
            print("|                                                         ")
            print(f'|      {linha.get("id")}- {linha.get("nome")}                  ')
            print("|                                                         ")
            print("-----------------------------------------------------------")

        escolha = int(input("Escolha uma máquina"))
        for count in resultados:

            if escolha == count.get("id"):

                return count.get("id")
            else:
                print("Máquina inválida")

def definir_componente(maquina):
    rep = True
    sql = f'SELECT id, tipo, descricao FROM componente where servidor_id = {maquina}'
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql) 
    resultados = cursor.fetchall()  
    cursor.close()
    while rep:
        for linha in resultados:
            print("-----------------------------------------------------------")
            print("|                   Selecione um componente                |")
            print("-----------------------------------------------------------")
            print("|                                                         ")
            print(f"|      {linha.get('id')}- {linha.get('tipo')}- {linha.get('descricao')}                  ")
            print("|                                                         ")
            print("-----------------------------------------------------------")

        escolha = int(input("Escolha um componente"))
        for count in resultados:

            if escolha == count.get("id"):
                return count.get("id")
            else:
                print("Componente inválida")

def definir_tempo():
        rep = True
        while rep:
            print("-----------------------------------------------------------")
            print("|                   Selecione um tempo                    |")
            print("-----------------------------------------------------------")
            print("|                                                         |")
            print(f"|                     entre 1 e 24 Horas                  |")
            print("|                                                         |")
            print("-----------------------------------------------------------")
            escolha = int(input("Escolha um tempo"))
            if escolha > 0 and escolha < 25:
                return escolha
                rep = False
            else:
                print("Tempo inválido")

def exibir(componente, interval):
    sql = f"SELECT AVG(valorDado) as valor, tipoDado, unidade FROM captura WHERE componente_id = {componente} AND dataFinal between date_sub(now(), interval {interval} hour) AND now() GROUP BY tipoDado, unidade;"
    captura_sql = f"Select AVG(timestampdiff(second, dataInicio, dataFinal)) as tempo from captura where dataFinal between date_sub(now(), interval {interval} hour) AND now() and componente_id = {componente};"
    print(interval)
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql)
    resultados = cursor.fetchall()  
    cursor.close()

    cursor = con.cursor(dictionary=True)
    cursor.execute(captura_sql) 
    resultado = cursor.fetchall()
    cursor.close()
    print(resultado)
    print(resultados)
    for linha in resultados:
        print("-----------------------------------------------------------")
        print("|                    Dados Registrados                    |")
        print("-----------------------------------------------------------")
        print("|                                                         |")
        print(f"|            Valor: {linha.get('valor'):.2f} {linha.get('unidade')}                             ")
        print(f"|            {linha.get('tipoDado')}                          ")

        print("|                                                         |")
        print("-----------------------------------------------------------")
    if len(resultado) == 0:
        print("Sem registro")
    else:
        print(f"Tempo médio de captura: {resultado[0].get('tempo')} segundos")

def exibir_geral(interval):
    sql = f"SELECT AVG(valorDado) as valor, tipoDado, unidade FROM captura WHERE dataFinal between date_sub(now(), interval {interval} hour) AND now() GROUP BY tipoDado, unidade;"
    captura_sql = f"Select AVG(timestampdiff(second, dataInicio, dataFinal)) as tempo from captura where dataFinal between date_sub(now(), interval {interval} hour) and now();"
    print(interval)
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql)
    resultados = cursor.fetchall()  
    cursor.close()

    cursor = con.cursor(dictionary=True)
    cursor.execute(captura_sql) 
    resultado = cursor.fetchall()
    cursor.close()



    for linha in resultados:
        print("-----------------------------------------------------------")
        print("|                    Dados Registrados                    |")
        print("-----------------------------------------------------------")
        print("|                                                         ")
        print(f"|                 Valor: {linha.get('valor'):.2f} {linha.get('unidade')}                       ")
        print(f"|                  {linha.get('tipoDado')}                     ")
        print("|                                                         ")
        print("-----------------------------------------------------------")
    if len(resultado) == 0:
        print("Sem registro")
    else:
        print(f"Tempo médio de captura: {resultado[0].get('tempo')} segundos")

def main():
    rep = True
    entrada = input("Digite sua senha")
    if entrada == senha:
        while rep:
        
        
            escolha = input("\nDeseja visualizar dados específicos ou uma média geral entre os servidores ? \n 1- Dados Específicos\n 2- Dados Gerais \n 3- Encerrar")
            if escolha == "1":
                maquina = definir_maquina()
                componente = definir_componente(maquina)
                print(componente)
                interval = definir_tempo()
                print(interval)
                exibir(componente, interval)
            elif escolha == "2":
                interval = definir_tempo()
                exibir_geral(interval)
            else:
                print("Programa encerrado")
                rep = False;    
    else:
        print("Senha incorreta")
        print("Programa encerrado")
        
main()
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
