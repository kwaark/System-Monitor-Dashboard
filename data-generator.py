from datetime import datetime
import os
import time
import matplotlib.pyplot as plt

# Verifica se o diretório "graficos" existe, caso contrário, cria-o
graficos_dir = "static/graficos"
if not os.path.exists(graficos_dir):
    os.makedirs(graficos_dir)

dates = []
mem_used = []
cpu_usage = []

# Função para atualizar os gráficos
def update_plots():
    print("Atualizando gráficos...")
    if len(dates) > 0 and len(mem_used) > 0:
        plt.figure(figsize=(10, 6))
        for i in range(1, len(dates)):
            plt.plot(dates[i-1:i+1], mem_used[i-1:i+1], 'b-')
        plt.xlabel("Date and Time")
        plt.ylabel("Usage (MB)")
        plt.title("Memory Usage Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(graficos_dir, "grafico_memoria.png"))
        plt.close()
        print(f"Gráfico de memória salvo em {graficos_dir}/grafico_memoria.png")

    if len(dates) > 0 and len(cpu_usage) > 0:
        plt.figure(figsize=(10, 6))
        for i in range(1, len(dates)):
            plt.plot(dates[i-1:i+1], cpu_usage[i-1:i+1], 'b-')
        plt.xlabel("Date and Time")
        plt.ylabel("Usage (%)")
        plt.title("CPU Usage Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(graficos_dir, "grafico_cpu.png"))
        plt.close()
        print(f"Gráfico de CPU salvo em {graficos_dir}/grafico_cpu.png")

# Leitura dos dados do arquivo e atualização dos gráficos
def read_data():
    print("Lendo dados...")
    with open("dados.txt", "r") as file:
        lines = file.readlines()

    for i in range(0, len(lines), 3):
        date_line = lines[i].strip()
        mem_line = lines[i+1].strip()
        cpu_line = lines[i+2].strip()

        date = datetime.strptime(date_line, "%d-%m-%Y %H:%M")
        mem_used_value = int(mem_line.split(": ")[2].split("MB")[0])
        cpu_usage_value = float(cpu_line.split(": ")[1].strip("%"))

        dates.append(date)
        mem_used.append(mem_used_value)
        cpu_usage.append(cpu_usage_value)

    update_plots()

# Loop for continuously updating the graphs
while True:
    read_data()
    # Wait a certain period of time before updating the graphs again
    # For example, wait 5 seconds before updating again
    time.sleep(5)