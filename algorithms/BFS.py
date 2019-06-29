from queue import Queue
from collections import defaultdict
from enum import Enum
import sys

from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix
from structs.graph import Graph
# from app.print_path_BFS import *

class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


class BFSAuxiliar():

    def __init__(self, vertexes):
        self.color = defaultdict(dict)
        self.d = defaultdict(dict)
        self.pi = defaultdict(dict)
        self.q_path = Queue()
        for i in vertexes:
            self.color[i] = Color.WHITE
            self.d[i] = float('inf')
            self.pi[i] = None
    @staticmethod
    def print_BFS(result, s):
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
                while result.pi[inc] is not None:
                    print(" <-- " + str(result.pi[inc]), end='')
                    inc = result.pi[inc]
                    len += result.d[inc]
                print("\n\tDistância:", len, end='')
        print("\n")
    def get_path(result, s):
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
                while result.pi[inc] is not None:
                    print(" <-- " + str(result.pi[inc]), end='')
                    inc = result.pi[inc]
                    len += result.d[inc]
                print("\n\tDistância:", len, end='')
        print("\n")

def change_auxiliar(aux: BFSAuxiliar, q: Queue, u, v):
    if aux.color[v] == Color.WHITE:
        aux.color[v] = Color.GRAY
        aux.d[v] = aux.d[u] + 1
        aux.pi[v] = u
        q.put(v)
        # aux.q_path.put(v)


def BFS(G: Graph, s):
    aux = BFSAuxiliar(G.vertexes)
    if s not in G.vertexes:
        return aux

    aux.color[s] = Color.GRAY
    aux.d[s] = 0
    aux.pi[s] = None

    q = Queue()
    q.put(s)

    while not(q.empty()):
        u = q.get()
        aux.q_path.put(u)
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

    
    # print(*aux.color)
    # print(*aux.d)
    # print(*aux.pi)
    return aux

    