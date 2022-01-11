import random 
from numpy import * 
# Importando a bliblioteca numpy
# O ambiente vai ser representado por uma matriz de 0 ou 1 podendo variar de tamanho
# que sera defenido na main. O valor 0 ou 1 que vai representar limpo ou sujo será
# definido aleatoriamente usando a função random. 

class Ambiente:
    def __init__(self,matriz):  
        self.matriz= matriz
    def matriz_amb(linha,coluna):      #Função matriz que gerará o ambiente para nosso agente.
        matriz =[]   
        num = [0,1]
        for i in range (0,linha):
            mlinha = []
            for j in range (0,coluna): 
                num_ale = random.choice(num)  # Numero aleatorio que é gerado pela função random
                mlinha.append(num_ale)        # Usando Append para adicionar na linha da matriz
            matriz.append(mlinha)
        print('A ambiente gerado foi: ',matriz,'\nSendo 0 o lugar limpo e 1 um local sujo!',
              '\nO aspirador de pó vai percorrer a matriz linha por linha da esquerda para a direita.\n')
        return(matriz)
        
        #Por fim, foi imprimido a matriz gerada.
        
        