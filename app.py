from napalm import get_network_driver
import os
import sys
from dotenv import load_dotenv
from menu import print_main_menu, print_banner
from functions import *


load_dotenv()
user = os.getenv('USER')
passwd = os.getenv('PASS')


#driver = get_network_driver('huawei_vrp')
#devices = []
#config = str()





if __name__ == "__main__":
    print_banner()

    

    while True:
        
        print_main_menu()
        
        option = int(input())

        if (option == 0):
            sys.exit()
        elif (option == 1):
            automation()
            
        elif (option == 2):
            pass
        elif (option == 3):
            pass
        else:
            print ("Opção inválida!")