from queue import Queue
from collections import defaultdict
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

    def __init__(self, vertexes):
        self.color = defaultdict(dict)
        self.d = defaultdict(dict)
        self.pi = defaultdict(dict)
        for i in vertexes:
            self.color[i] = Color.WHITE
            self.d[i] = float('inf')
            self.pi[i] = None


def change_auxiliar(aux: DFSAuxiliar, q: Queue, u, v):
    if aux.color[v] == Color.WHITE:
        aux.color[v] = Color.GRAY
        aux.d[v] = aux.d[u] + 1
        aux.pi[v] = u
        q.put(v)


def BFS(G: Graph, s):
    aux = DFSAuxiliar(G.vertexes)
    if s not in G.vertexes:
        return aux

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
                v = current.get_index()
                change_auxiliar(aux, q, u, v)
                current = current.get_next()
        else:
            if isinstance(G, AdjMatrix):
                for v in G.vertexes[u]:
                    change_auxiliar(aux, q, u, v)
        aux.color[u] = Color.BLACK

    # print(aux.color)
    # print(aux.d)
    # print(aux.pi)
    return aux
