# A classe agente contém as funcionalidades de um aspirador de pó.
# No caso mostrado é um agente reativo simples, ele simplismente vai reagir aos eventos
# de acordo com as regras já pre-estabelecidas no codigo.

class Agente:
    def __init__(self,matriz):
         self.matriz= matriz
    
    def aspirar (matriz):       # A função aspirar ela percorre a matriz e ao percorrer altera ou não o estado do local
                                # ele percorrer a matriz linha por linha da esquerda para a direita
        local=matriz[:]         # A letra 'x' representa o local em que o agente está.
        for i in range (len(matriz)):
            for j in range (len(matriz[i])):
                if (matriz[i][j]==1):             #Se ele entrar nessa condição o agente irá alterar o numero do ambiente que será um local sujo
                    print('Percorrendo a linha',matriz[i])   
                    local[i][j] ='x'
                    print('Aspirando a posicao',matriz[i])
                    matriz[i][j] = 0                                  # O valor que era 1 foi limpo e agora será 0
                    print('\033[1;31mO local estava sujo e foi limpo!\033[m', matriz[i],'\n')

                else:   #Se não ele ira entrar na outra condição e apenas continuará percorrendo na matriz
                    print('Percorrendo a linha',matriz[i]) 
                    local[i][j] ='x'                       
                    print('Percorrendo a posicao',matriz[i])
                    matriz[i][j] = 0                       #O lugar nao se altera
                    print('\033[1;32mEste local está limpo!\033[m',matriz[i],'\n')     

            print('\n')                
                    
        
    