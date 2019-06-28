from collections import defaultdict
from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix
from structs.graph import Graph
from app.print_path_bellman_ford import *
# from app.minimum_path import *


class BellmanFordAux(object):
    
    def __init__(self, G: Graph, s):
        self.d = defaultdict(dict)
        self.pi = defaultdict(dict)
        self.loop = None
        for i in G.vertexes:
            self.d[i] = float('inf')
            self.pi[i] = None
        if s in G.vertexes:
            self.d[s] = 0

    def print_bellman_ford(result, s):
        if result.loop == True:
            print('Há loop negativo, portanto, resposta não confiável')
        elif result.loop == False:
            print('Não há loop negativo, portanto, resposta confiável')
        for u in result.d:
            print("Vértice:", u)

            if result.pi[u] is None and u == s:
                print("Caminho: Raiz", end='')
            else:
                if result.pi[u] is None:
                    print("Não são conectados", end='')
                else:
                    print("Caminho:", u, end='')
                    inc = u
                    len = result.d[inc]
                    # print(result.d[inc])
                    # input()
                    while result.pi[inc] is not None:
                        print(" <-- " + str(result.pi[inc]), end='')
                        inc = result.pi[inc]
                        # len += result.d[inc]
                    print("\n\tDistância:", len, end='')
            print("\n")
            # print_path(self, s)


def relax(aux: BellmanFordAux, u, v, w: int):
    if aux.d[v] > (aux.d[u]+w):
        aux.d[v] = aux.d[u] + w
        aux.pi[v] = u


def bellman_ford(G: Graph, s):
    aux = BellmanFordAux(G, s)

    for u in G.vertexes:
        if isinstance(G, AdjMatrix):
            for v in G.vertexes[u]:
                relax(aux, u, v, G.get_value(u, v))
        else:
            cur = G.vertexes[u]
            while cur is not None:
                relax(aux, u, cur.get_index(), cur.get_value())
                cur = cur.get_next()

    for u in G.vertexes:
        if isinstance(G, AdjMatrix):
            for v in G.vertexes[u]:
                if aux.d[v] > (aux.d[u] + G.get_value(u, v)):
                    aux.loop = False
                    return aux
        else:
            cur = G.vertexes[u]
            while cur is not None:
                if aux.d[cur.get_index()] > (aux.d[u] + cur.get_value()):
                    aux.loop = False
                    return aux
                cur = cur.get_next()

    aux.loop = True
    return aux

