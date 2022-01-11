print(""" GRUPO 8
 Inteligência Artificial
 Professor: Alex Oliveira Barradas Filho
 Aluno: João Felipe Melo da luz                     Matricula: 2019004732
 Aluno:Carlos Eduardo Nascimento  Cajado            Matricula: 2019004536
 Aluno:Marcos Vinicius Correia  Leite               Matricula: 2016046686

   ALGORITMO A* (A ESTRELA)
   """)


from busca import *

if __name__ == '__main__':

    labirinto = [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]]

    inicio = [0, 0]  # inicio  posicao
    fim = [4, 10]  # fim da posicao
    cost = 1  # constante movimento
    print('\n')
    path = busca(labirinto, cost, inicio, fim)
    print(f'O Ponto de partida é{inicio} e O Destino é {fim}\n')
    print(f'O LABIRINTO INICIAL É :\n{labirinto}\n')


print("A TRAJETÓRIA SERÁ:\n")
print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row])
      for row in path]))
