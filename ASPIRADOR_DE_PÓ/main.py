# GRUPO 8                                       
# Inteligência Artificial                                                                                     
# Professor: Alex Oliveira Barradas Filho                                                        
# Aluno: João Felipe Melo da luz                     Matricula: 2019004732                       
# Aluno:Carlos Eduardo Nascimento  Cajado            Matricula: 2019004536                                                      
# Aluno:Marcos Vinicius Correia  Leite               Matricula: 2016046686

from ambiente import * 
from Agente import *
## importa os 2 arquivos que tem a classe agente e ambiente e suas funções.

class LigarApirador: 
    def __init__(self, agente, ambiente):
        self.agente = agente
        self.ambiente = ambiente
    def controlar ():
        amb= Ambiente.matriz_amb(3,3)    # Aqui poderá ser alterado o tamanho da matriz que será recebida na classe Ambiente e irá escolher os valores 0 ou 1 aleatoriamente.
        print(Agente.aspirar(amb))       # Será printado a função do agente aspirar que irá percorrer toda a matriz.
        
        return ('Limpou tudo')
    
print(LigarApirador.controlar())