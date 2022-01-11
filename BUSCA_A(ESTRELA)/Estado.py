import numpy as np
from trajetoria import *


class Node:
    """ A *(estrela ) é é um dos algoritmos de pesquisa mais bem-sucedidos, pois posui a capacidade
    de encontrar o caminho mais curto entre as barrreiras.

        posicao é a posicao atual do Nodo no labirinto
        g é o custo do início ao nó atual
        h é o custo estimado com base heurística para o nó atual para o nó final
        f é o custo total do nó presente, ou seja: f = g + h
    """

    def __init__(self, princial=None, posicao=None):
        self.princial = princial
        self.posicao = posicao

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.posicao == other.posicao
