from datetime import timedelta
import threading
import mysql.connector
import time
import psutil
import keyboard

from datetime import datetime


con = mysql.connector.connect(
   host="localhost", 
   user="usuario_inseridor", 
   passwd="inseridor123", 
   db="opticar",
)

servidor_id = None

componentes_ids =  {
        
        "cpu": None,
        "ram" : None,
        "disco": None,
        "rede" : None
}
## CAPTURAR COMPONENTES DE ACORDO COM O ID DO SERVIDOR
while True:
    servidor_id = input("Digite o Id do servidor:")
    if(servidor_id.isalnum()):
        cursor = con.cursor(dictionary=True)
        sql = f"SELECT REPLACE(tipo,' ','') as tipo, id FROM componente WHERE servidor_id = {servidor_id}"
        cursor.execute(sql)
        componentes = cursor.fetchall()
        
        
        cursor.close()
        if len(componentes) > 0:
            for componente in componentes:
                print(componente.get("tipo") == "PlacadeRede")
                if componente.get("tipo") == "CPU":
                    id_cpu = componente.get("id")
                    componentes_ids.update(cpu=id_cpu)            
                elif componente.get("tipo") == "RAM":
                    id_ram = componente.get("id")
                    componentes_ids.update(ram=id_ram)
                elif componente.get("tipo") == "Disco":
                    id_disco = componente.get("id")
                    componentes_ids.update(disco=id_disco)            
                elif componente.get("tipo") == "PlacadeRede":
                    
                    id_rede = componente.get("id")
                    print(id_rede)
                    componentes_ids.update(rede=id_rede)            
            break
# TRAZER AS METRICAS DE ALERTA DA EMPRESA 
def trazer_metricas():
    cursor = con.cursor(dictionary=True)
    sql = f"""
    SELECT tipoMetrica, limiteCritico, limiteAtencao FROM alerta_config AS ac
    JOIN empresa e
    ON ac.empresa_id = e.id
    JOIN fabrica f
    ON e.id = f.empresa_id
    JOIN servidor s 
    ON f.id = s.fabrica_id
    WHERE s.id = {servidor_id};
    SELECT * from alerta_config;
    """
    cursor.execute(sql)
    METRICAS_ALERTA = cursor.fetchall()
    
    cursor.close()

    print(METRICAS_ALERTA)













def zerar_tempo():
    return  datetime.now().strftime("%Y-%m-%d %H:%M:%S")



stop_event = threading.Event()


def monitoramento():
    while not stop_event.is_set():
        time.sleep(1) 

        # Coletando dados do sistema
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disco = psutil.disk_usage('C:/').percent
        # Captura os dados iniciais
        disk_io_antes = psutil.disk_io_counters()
        time.sleep(1)  # Intervalo de tempo para medir a taxa

        # Captura os dados depois de 1 segundo
        disk_io_depois = psutil.disk_io_counters()

        # Calcula a diferença
        tempo_intervalo = 1  # Intervalo de tempo em segundos
        disco_tempo_Leitura = (disk_io_depois.read_bytes - disk_io_antes.read_bytes) / (tempo_intervalo * 1024**2)
        disco_tempo_Leitura = round(disco_tempo_Leitura, 1)
        disco_tempo_Escrita = (disk_io_depois.write_bytes - disk_io_antes.write_bytes) / (tempo_intervalo * 1024**2)
        disco_tempo_Escrita = round(disco_tempo_Escrita, 1)
        rede_leitura = round(psutil.net_io_counters().bytes_recv / (1024**2), 2)
        rede_escrita = round(psutil.net_io_counters().bytes_sent / (1024**2), 2)    

        if stop_event.is_set():
            return
        # Exibindo os dados
        print("-------------------------------")
        print("|         MONITORAMENTO!      |")
        print("-------------------------------")
        print(f"|        Uso Cpu {cpu} %       |")
        print(f"|        Uso Ram {ram} %       |")
        print(f"|       Uso Disco {disco} %      |")
        print(f"| Disco Tempo Leitura {disco_tempo_Leitura} MB/s|")
        print(f"| Disco Tempo Escrita {disco_tempo_Escrita} MB/s|") 
        print(f"| Rede Tempo Leitura {rede_leitura} GB |")
        print(f"| Rede Tempo Escrita {rede_escrita} GB |")
        print("-------------------------------")


def dados(escolha):
    if escolha == "1":
        intervalo = 5  
    elif escolha == "2":
        intervalo = 30  
    else:
        intervalo = 60  

    hora_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    count = intervalo
    mediaCPU = 0
    mediaDiscoL = 0
    mediaDiscoE = 0
    while not stop_event.is_set():
        cpu_list = []
        disco_leitura_list = []
        disco_escrita_list = []
        
        for _ in range(intervalo):
            if stop_event.is_set():
                return
            
            time.sleep(1)
            cpu_list.append(psutil.cpu_percent(interval=1))
            
            disk_io_antes = psutil.disk_io_counters()
            time.sleep(1)
            disk_io_depois = psutil.disk_io_counters()
            
            tempo_intervalo = 1
            disco_leitura_list.append((disk_io_depois.read_bytes - disk_io_antes.read_bytes) / (tempo_intervalo * 1024**2))
            disco_escrita_list.append((disk_io_depois.write_bytes - disk_io_antes.write_bytes) / (tempo_intervalo * 1024**2))
        
        cpu = round(sum(cpu_list) / len(cpu_list), 2)
        disco_tempo_Leitura = round(sum(disco_leitura_list) / len(disco_leitura_list), 1)
        disco_tempo_Escrita = round(sum(disco_escrita_list) / len(disco_escrita_list), 1)
        ram = psutil.virtual_memory().percent
        disco = psutil.disk_usage('C:/').percent
        rede_leitura = round(psutil.net_io_counters().bytes_recv / (1024**2), 2)
        rede_escrita = round(psutil.net_io_counters().bytes_sent / (1024**2), 2)

        if stop_event.is_set():
            return 
    
        print("-------------------------------")
        print("|      Dados Armazenados!     |")
        print("-------------------------------")
        print(f"|        Uso Cpu {cpu} %       |")
        print(f"|        Uso Ram {ram} %       |")
        print(f"|       Uso Disco {disco} %      |")
        print(f"| Disco Tempo Leitura {disco_tempo_Leitura} MB/s|")
        print(f"| Disco Tempo Escrita {disco_tempo_Escrita} MB/s|") 
        print(f"| Rede Tempo Leitura {rede_leitura} MB/s |")
        print(f"| Rede Tempo Escrita {rede_escrita} MB/s |")
        print("-------------------------------")
        
        dados  = [
            {
                "valor": cpu,
                "tipo": "Uso CPU",
                "id_componente": componentes_ids.get('cpu'),
                "unidade": '%'
            },
            {
                "valor":ram,
                "tipo": "Uso RAM",
                "id_componente": componentes_ids.get('ram'),
                "unidade": '%'
            },
            {
                "valor": disco,
                "tipo": "Uso DISCO",
                "id_componente": componentes_ids.get('disco'),
                "unidade": '%'
            },
            {
                "valor": disco_tempo_Leitura,
                "tipo": "DISCO Tempo Leitura",
                "id_componente": componentes_ids.get('disco'),
                "unidade": 'MB/s'
            },
            {
                "valor": disco_tempo_Escrita,
                "tipo": "DISCO Tempo Escrita",
                "id_componente": componentes_ids.get('disco'),
                "unidade": 'MB/s'
            },
            {
                "valor": rede_leitura,
                "tipo": "REDE Tempo Leitura",
                "id_componente": componentes_ids.get('rede'),
                "unidade": 'MB/s'
            },
            {
                "valor":rede_escrita,
                "tipo": "REDE Tempo Escrita",
                "id_componente": componentes_ids.get('rede'),
                "unidade": 'MB/s'
            }
        ]

        # horaInicio = hora_inicio
        sql = 'INSERT INTO captura (valorDado, tipoDado,  componente_id, unidade, dataInicio) VALUES (%s, %s,%s,%s,%s)'
        cursor = con.cursor()
        ids_inseridos = []
        for dado in dados:

            cursor.execute(sql, (dado.get('valor'), dado.get('tipo'), dado.get('id_componente'), dado.get('unidade'), hora_inicio))
            ids_inseridos.append(cursor.lastrowid)
            print(ids_inseridos)
        con.commit()
        hora_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        


# Menu principal
print("-----------------------------------------------------------")
print("|             Escolha um intervalo de captura             |")
print("-----------------------------------------------------------")
print("|  teste(5 segundos)   teste(30 segundos)   teste(1 min)  |")
print("| 1- Cenário Crítico  2- Cenário Regular  3- Cenário Leve |")
print("|     (15min)               (30min)           (60min)     |")
print("-----------------------------------------------------------")

escolha = input()  


historico = threading.Thread(target=dados, args=(escolha,))
monitoramento_thread = threading.Thread(target=monitoramento)

trazer_metricas()

historico.start()
monitoramento_thread.start()


print("\nPressione 'q' para sair...")
while True:
    if keyboard.is_pressed("q"):  
        print("\nEncerrando monitoramento...")
        stop_event.set()
        break

historico.join()
monitoramento_thread.join()

print("Monitoramento finalizado.")


