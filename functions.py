from menu import print_automation_menu
import os
import subprocess
import paramiko
from paramiko.ssh_exception import AuthenticationException, SSHException
import time
from dotenv import load_dotenv



def create_file(path, file_name):

    if not file_name.endswith(".txt"):
        file_name +='.txt'

    # Define caminho + nome do arquivo
    file_path= os.path.join(path, file_name)

    # 2. Garante que a pasta existe
    os.makedirs(path, exist_ok=True)


    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("")

    if os.name == 'nt': #Se o SO for Windows
        subprocess.run(['notepad.exe', file_path])
    else: # Se não for Windows
        subprocess.run(['nano', file_path])

    if os.path.exists(file_path):
        print(f"\n[+] Arquivo '{file_name}' criado com sucesso!")
    else:
        print("\n[!] Criação cancelada ou arquivo não salvo.")


def search_file(full_path, path):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    if not full_path:
        print("\n[!] Nanhum arquivo encontrado...")
        return

    else:
        print("\n--- SELECIONE UM ARQUIVO ---")
        print()
        print("[0] - Voltar")
        print()

        for i, nome in enumerate(full_path, 1):
            print(f'[{i}] {nome}')

        try:
            file = int(input())
            if file ==  0:
                return
            else:

                if file >= 1 and file <= len(full_path):
                    config_file = full_path[file-1]
                    print()
                    print(f"Selecionado: {config_file}")
                    full_path_file = os.path.join(BASE_DIR, path, config_file)
                    return full_path_file
                else:
                    print()
                    print(f"Erro: O índice {file} não existe. Escolha entre 1 e {len(path)}.")
        except ValueError:
            print("Erro: Digite apenas números!")
            return


def automation():

    host_file = None
    config_file = None

    while True:

        print_automation_menu(config_file, host_file)
        
        option = int(input())

        if (option == 0):
            return
        elif (option == 1):

            files = os.listdir("./hosts")
            host_file = search_file(files, "hosts")
           
        elif (option == 2):
            files = os.listdir("./configs")
            config_file = search_file(files, "configs")

        elif (option == 3):

            load_dotenv()
            user = os.getenv('USER')
            passwd = os.getenv('PASS')

            if host_file is None or config_file is None:
                print()
                print ("Antes de executar uma automação, selecione os arquivos de configuração e hosts")

            else:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                hosts, configs = [], []

                #CARREGA OS HOSTS EM UMA LISTA DE HOSTS
                with open(host_file, 'r', encoding='utf-8') as file_host:
                    for line in file_host:
                        line_host = line.strip()
                        if line_host:
                            hosts.append(line_host)
                
                #CARREGA CADA LINHA DE CONFIGURAÇÃO EM UMA LISTA
                with open(config_file, 'r', encoding='utf-8') as file_config:
                    for line in file_config:
                        line_config = line.strip()
                        if line_config:
                            configs.append(str(line_config))

                for host in hosts:

                    try:
                            
                        client.connect(host, username=user, password=passwd, timeout=10)
                        shell = client.invoke_shell()
                        time.sleep(1)
                        
                        for config in configs:
                            shell.send(config + '\n')
                            time.sleep(0.5) 

                        client.close()
                        print(f'host {host} configurado com sucesso!!!')

                    except AuthenticationException:
                        print(f"[!] ERRO DE AUTENTICAÇÃO: Usuário ou senha incorretos para o host {host}.")
                        continue 

                    except SSHException as e:
                        print(f"[!] ERRO DE SSH: Problema de conexão ou algoritmo incompatível em {host}: {e}")
                        continue

                    except Exception as e:
                        print(f"[!] Erro ao configurar {host}: {e}")