from menu import print_automation_menu
import os
def automation():

    while True:
        print_automation_menu()
        
        option = int(input())

        if (option == 0):
            return
        elif (option == 1):

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
                

                try:
                    file = int(input())
                    if file == 0:
                        continue
                    else:
                    
                        if file >= 1 and file <= len(files):
                            host_file = files[file-1]
                            print()
                            print(f"Selecionado: {host_file}")
                        else:
                            print()
                            print(f"Erro: O índice {file} não existe. Escolha entre 1 e {len(files)}.")
                    
                except ValueError:
                    print("Erro: Digite apenas números!")
                    continue

        elif option == 2:
            print("optinon 2")
            
        elif option == 3:
            print("optinon 3")