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
   db="py",
)


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
        print(f"| Rede Tempo Leitura {rede_leitura} GB|")
        print(f"| Rede Tempo Escrita {rede_escrita} GB|")
        print("-------------------------------")


def dados(escolha):
    if escolha == "1":
        intervalo = 5  
    elif escolha == "2":
        intervalo = 30  
    else:
        intervalo = 60  

    sql = 'INSERT INTO hardware (cpu_percent, ram_percent, disco_percent, disco_leitura, disco_escrita, rede_leitura, rede_escrita) VALUES (%s,%s,%s,%s,%s,%s,%s)'

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
        print(f"| Rede Tempo Leitura {rede_leitura} GB|")
        print(f"| Rede Tempo Escrita {rede_escrita} GB|")
        print("-------------------------------")

        cursor = con.cursor()
        cursor.execute(sql, (cpu, ram, disco, disco_tempo_Leitura, disco_tempo_Escrita, rede_leitura, rede_escrita))
        con.commit()

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
