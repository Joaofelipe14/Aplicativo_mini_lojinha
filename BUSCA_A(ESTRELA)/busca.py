from Estado import *


def busca(labirinto, cost, inicio, fim):
    """
        Returns a list of tuples as a path from the given inicio to the given fim in the given labirinto
        :param labirinto:
        :param cost
        :param inicio:
        :param fim:
        :return:
    """

    #  É Criado o  inicio e nó fim com valores iniciados para g, h e f
    inicio_node = Node(None, tuple(inicio))
    inicio_node.g = inicio_node.h = inicio_node.f = 0
    fim_node = Node(None, tuple(fim))
    fim_node.g = fim_node.h = fim_node.f = 0

    #Encontraremos o nó de menor custo para expandir
    ainda_verificado_lista = []

    verificado_lista = []

    # adicinando inicio nó
    ainda_verificado_lista.append(inicio_node)

    # Adicionando uma condição de parada. Isso é para evitar qualquer loop infinito
    # execução após um número razoável de etapas
    outer_iterations = 0
    max_iterations = (len(labirinto) // 2) ** 10

    # movimento serarca é esquerda-direita-cima-baixo
    #  com (4 movimentos) de cada posição

    move = [[-1, 0],  # subir
            [0, -1],  # esquerda
            [1, 0],  # descer
            [0, 1]]  # direita

    #labirinto definido o numero linhas e colunas
    no_linhas, no_colunas = np.shape(labirinto)

    #  loop até o fim

    while len(ainda_verificado_lista) > 0:
        outer_iterations += 1

        # colocamos lugar_atual do nó
        lugar_atual_node = ainda_verificado_lista[0]
        lugar_atual_index = 0
        for index, item in enumerate(ainda_verificado_lista):
            if item.f < lugar_atual_node.f:
                lugar_atual_node = item
                lugar_atual_index = index

        if outer_iterations > max_iterations:
            print("giving up on pathfinding too many iterations")
            return return_path(lugar_atual_node, labirinto)

        ainda_verificado_lista.pop(lugar_atual_index)
        verificado_lista.append(lugar_atual_node)

# testar se a meta foi atingida ou não, se sim, retorne o caminho
        if lugar_atual_node == fim_node:
            return return_path(lugar_atual_node, labirinto)

# Gerar filho de todos os quadrados adjacentes
        filho = []

        for new_posicao in move:
            # nó posicao
            node_posicao = (
                lugar_atual_node.posicao[0] + new_posicao[0], lugar_atual_node.posicao[1] + new_posicao[1])

            # Verificando se está detro do labirinto
            if (node_posicao[0] > (no_linhas - 1)
                or node_posicao[0] < 0
                or node_posicao[1] > (no_colunas - 1)
                    or node_posicao[1] < 0):
                continue

            # verificando se a area pode ser percorrida
            if labirinto[node_posicao[0]][node_posicao[1]] != 0:
                continue

            # criando um novo nó
            new_node = Node(lugar_atual_node, node_posicao)
            filho.append(new_node)

        # Loop filho
        for crianca in filho:

            # buscando em toda a lista
            if len([verificado_filho for verificado_filho in verificado_lista if verificado_filho == crianca]) > 0:
                continue

            # Crie os valores f, g e hs
            crianca.g = lugar_atual_node.g + cost
            # usando a distância euclediana, é calculado o custo
            crianca.h = (((crianca.posicao[0] - fim_node.posicao[0]) ** 2)
                         + ((crianca.posicao[1] - fim_node.posicao[1]) ** 2))

            crianca.f = crianca.g + crianca.h

            if len([i for i in ainda_verificado_lista if crianca == i and crianca.g > i.g]) > 0:
                continue

            # colocando a criança ainda_verificado_lista
            ainda_verificado_lista.append(crianca)
