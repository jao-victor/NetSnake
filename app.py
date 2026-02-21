from napalm import get_network_driver
import os
import sys
from dotenv import load_dotenv
from menu import print_main_menu, print_banner, limpar_tela
from functions import *


load_dotenv()
user = os.getenv('USER')
passwd = os.getenv('PASS')



if __name__ == "__main__":
    print_banner()

    while True:
        print_main_menu()
        
        try:
            option = int(input())

            if (option == 0):
                sys.exit()
                
            elif (option == 1):
                limpar_tela()
                automation()
                
            elif (option == 2):
                path = "./configs"
                name_file = input("Digite o nome do arquivo de configuração:").strip()
                create_file(path, name_file)

            elif (option == 3):
                path = "./hosts"
                name_file = input("Digite o nome do arquivo de Hosts:").strip()
                create_file(path, name_file)

            else:
                print ("Opção inválida!")
        except ValueError:
            print("Apenas números, por favor...")