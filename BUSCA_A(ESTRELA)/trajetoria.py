from Estado import *


def return_path(lugar_atual_node, labirinto):
    path = []
    no_linhas, no_colunas = np.shape(labirinto)
    # criamos o labirinto
    resultado = [[-1 for i in range(no_colunas)] for j in range(no_linhas)]
    lugar_atual = lugar_atual_node
    while lugar_atual is not None:
        path.append(lugar_atual.posicao)
        lugar_atual = lugar_atual.princial
    #  é criado o labirinto e iniciado com -1 para cada posição
    path = path[::-1]
    inicio_value = 0
    # atualizamos o caminho de inicio para fim r com cada passo  1
    for i in range(len(path)):
        resultado[path[i][0]][path[i][1]] = inicio_value
        inicio_value += 1
    return resultado
