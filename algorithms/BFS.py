from queue import Queue
from enum import Enum
import sys

from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix
from structs.graph import Graph


class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


class DFSAuxiliar():

    def __init__(self, len):
        self.color = []
        self.d = []
        self.pi = []
        for i in range(0, len):
            self.color.append(1)
            self.d.append(None)
            self.pi.append(None)


def change_auxiliar(aux: DFSAuxiliar, q: Queue, u, v):
    if aux.color[v] == Color.WHITE:
        aux.color[v] = Color.GRAY
        aux.d[v] = aux.d[u] + 1
        aux.pi[v] = u
        q.put(v)


def BFS(G: Graph, s):
    aux = DFSAuxiliar(G.len)
    for u in range(0, G.len):
        if s == u:
            continue

        aux.color[u] = Color.WHITE
        aux.d[u] = sys.maxsize
        aux.pi[u] = None

    aux.color[s] = Color.GRAY
    aux.d[s] = 0
    aux.pi[s] = None

    q = Queue()
    q.put(s)

    while not(q.empty()):
        u = q.get()
        if isinstance(G, AdjList):
            current = G.vertexes[u]
            while current is not None:
                v = current.get_val()
                change_auxiliar(aux, q, u, v)
                current = current.get_prox()
        else:
            if isinstance(G, AdjMatrix):
                for v in G.vertexes[u]:
                    # Tem essa parte ainda???
                    # if G.vertexes[u][v] == 0:
                    #     continue

                    change_auxiliar(aux, q, u, v)
        aux.color[u] = Color.BLACK

    # print(aux.color)
    # print(aux.d)
    # print(aux.pi)
    return aux
