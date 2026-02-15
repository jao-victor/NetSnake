from menu import print_automation_menu
import os
def automation():
    print_automation_menu()
    
    option = int(input())

    if (option == 0):
        return
    elif (option == 1):

        while True:
            files = os.listdir("./hosts")

            if not files:
                print("\n[!] Nanhum arquivo encontrado...")
                continue

            else:
                print("\n--- SELECIONE UM ARQUIVO DE HOSTS ---")
                print()
                print("[0] - Voltar")
                print()
                for i, nome in enumerate(files, 1):
                    print(f'[{i}] {nome}')
                
                file = int(input())


                try:
                    if file > 1 and file <= len(files):
                        host_file = files[file-1]
                        print()
                        print(f"Selecionado: {host_file}")
                        return host_file
                    else:
                        print()
                        print(f"Erro: O índice {file} não existe. Escolha entre 1 e {len(files)}.")
                except ValueError:
                    print("Erro: Digite apenas números!")
                    return None
            
    elif option == 2:
        pass
    elif option == 3:
        pass