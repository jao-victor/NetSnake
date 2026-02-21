from menu import print_automation_menu
import os
import subprocess

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


def search_file(path):

    if not path:
        print("\n[!] Nanhum arquivo encontrado...")
        return

    else:
        print("\n--- SELECIONE UM ARQUIVO ---")
        print()
        print("[0] - Voltar")
        print()

        for i, nome in enumerate(path, 1):
            print(f'[{i}] {nome}')

        try:
            file = int(input())
            if file ==  0:
                return
            else:

                if file >= 1 and file <= len(path):
                    config_file = path[file-1]
                    print()
                    print(f"Selecionado: {config_file}")
                    return config_file
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
            host_file = search_file(files)
           
        elif (option == 2):
            files = os.listdir("./configs")
            config_file = search_file(files)

        elif (option == 3):

            if host_file is None or config_file is None:
                print()
                print ("Antes de executar uma automação, selecione os arquivos de configuração e hosts")
            else:
                pass