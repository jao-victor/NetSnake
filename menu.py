import os


def print_automation_menu():
    limpar_tela()
    print()
    print()
    print()
    print("=" * 50)
    print(f"{'GERENCIADOR DE AUTOMAÇÃO':^50}")
    print("=" * 50)
    print("  [1] - Selecionar Arquivo de Host")
    print("  [2] - Selecionar Arquivos de Configuração")
    print("  [3] - Definir Configuração")
    print("  [4] - Definir Hosts")
    print("  [5] - Executar Automação")
    print("  [6] - Ajuda")
    print("-" * 50)
    print("  [0] - Voltar / Sair")
    print("=" * 50)
    print()
    print()
    print()


def print_main_menu():

    print()
    print()
    print()
    print("=" * 40)
    print(f"{'MENU':^40}")
    print("=" * 40)
    print("  [1] - Automações")
    print("  [2] - Criar Arquivo de Configuração")
    print("  [3] - Criar Arquivo de Host")
    print("-" * 40)
    print("  [0] - Sair")
    print("=" * 40)
    print()
    print()
    print()
    

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')



def print_banner():
    logo = """                                                                 
                                     =*%@@@@@@@@@@@@@@@@#*-                                         
                                 *@@@@@@@@@@@@@@@@@@@@@@@@@@@@=                                     
                             :#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.                                 
                          .#@@@@@@@@*%@@@@@@@@@@@@@@@@@@@@%*@@@@@@@@*                               
                        -@@@@@@@@@@@@.=@@@@@@@@@@@@@@@@@%.=@@@@@@@@@@@%.                            
                      +@@@@@@@@@@@@@@#  :%@@@@@@@@@@@@#  .@@@@@@@@@@@@@@%:                          
                    =@@@@@@*      :*@@@@@@@@@%@@@@@@@@@@@@@%+.     :#@@@@@@:                        
                  :@@@@@@#   :%@@@*-  *@@@@@@@@@@@@@@@@@@=  =#@@@#   .%@@@@@#                       
                  *@@@@@%        -@@@*  #@@@@@@@@@@@@@@* .@@@%.       -@@@@@@:                      
                  *@@@@@*          .%@@.  #@+-    -+@=  -@@*           @@@@@@=                      
                 :@@@@@@*            *@#  @-        ==  %@-            @@@@@@@                      
                  #@@@@@#             %@- :          . +@=            .@@@@@@+                      
                  #@@@@@@              @#             .@*             +@@@@@@*                      
                  -@@@@@@#             :@+            %%.             %@@@@@@                       
                  .@@@@@@@=             +@=          *@-             +@@@@@@#                       
                    @@@@@@@-             *@%#*****#%@@:             +@@@@@@#                        
                    :@@@@@@@-             :%@@@#%@@@#              *@@@@@@@.                        
                     *@@@@@@@*                                    #@@@@@@@=                         
                      *@@@@@@@#                                  @@@@@@@@-                          
                      *@@@@@@@@@                               -@@@@@@@@@-                          
                        *@@@@@@@@:                            +@@@@@@@@=                            
                         *@@@@@@@@:                          +@@@@@@@@:                             
                          *@@@@@@@@.                        +@@@@@@@@=                              
                           *@@@@@@@@                       :@@@@@@@@+                               
                            %@@@@@@@+                      #@@@@@@@+                                
                             %@@@@@@%.                    -@@@@@@@+                                 
                              %@@@@@@-                    %@@@@@@*                                  
                               %@@@@@*                    @@@@@@%                                   
                               .@@@@@%                   -@@@@@#                                    
                                 @@@@@                   =@@@@#                                     
                                 :@@@@                   =@@@@                                      
                                  =@@@                   =@@@.                                      
                                   #@%                   -@@:                                       
                                    %#                   .@*                                        
                                    :+                    %.                                        
    """
    name = """
         .S_sSSs      sSSs  sdSS_SSSSSSbs                sSSs   .S_sSSs     .S_SSSs     .S    S.     sSSs  
        .SS~YS%%b    d%%SP  YSSS~S%SSSSSP               d%%SP  .SS~YS%%b   .SS~SSSSS   .SS    SS.   d%%SP  
        S%S   `S%b  d%S'         S%S                   d%S'    S%S   `S%b  S%S   SSSS  S%S    S&S  d%S'    
        S%S    S%S  S%S          S%S                   S%|     S%S    S%S  S%S    S%S  S%S    d*S  S%S     
        S%S    S&S  S&S          S&S                   S&S     S%S    S&S  S%S SSSS%S  S&S   .S*S  S&S     
        S&S    S&S  S&S_Ss       S&S                   Y&Ss    S&S    S&S  S&S  SSS%S  S&S_sdSSS   S&S_Ss  
        S&S    S&S  S&S~SP       S&S                   `S&&S   S&S    S&S  S&S    S&S  S&S~YSSY%b  S&S~SP  
        S&S    S&S  S&S          S&S                     `S*S  S&S    S&S  S&S    S&S  S&S    `S%  S&S     
        S*S    S*S  S*b          S*S                      l*S  S*S    S*S  S*S    S&S  S*S     S%  S*b     
        S*S    S*S  S*S.         S*S                     .S*P  S*S    S*S  S*S    S*S  S*S     S&  S*S.    
        S*S    S*S   SSSbs       S*S                   sSS*S   S*S    S*S  S*S    S*S  S*S     S&   SSSbs  
        S*S    SSS    YSSP       S*S                   YSS'    S*S    SSS  SSS    S*S  S*S     SS    YSSP  
        SP                       SP                            SP                 SP   SP                  
        Y                        Y                             Y                  Y    Y                   
    """

    print(logo)
    print(name)