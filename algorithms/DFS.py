from enum import Enum
from collections import defaultdict
from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix
from structs.graph import Graph


class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


class DFSAuxiliar():
    c_root = None

    def __init__(self, vertexes):
        self.color = []
        self.d = defaultdict(dict)
        self.f = defaultdict(dict)
        self.r = defaultdict(dict)
        for i in vertexes:
            self.color[i] = Color.WHITE


def DFS_VISIT(G: Graph, aux: DFSAuxiliar, u: int, time: int):
    aux.color[u] = Color.GRAY
    time += 1
    aux.d[u] = time
    aux.r[aux.c_root] = u  # labels the vertexes

    if isinstance(G, AdjMatrix):
        for v in G.vertexes[u]:
            if (G.vertexes[u][v] == 1) & (aux.color[v] == Color.WHITE):
                time = DFS_VISIT(G, aux, v, time)
    else:
        cur = G.vertexes[u]
        while cur is not None:
            if aux.color[cur.get_val()] == Color.WHITE:
                time = DFS_VISIT(G, aux, cur.get_val(), time)
            cur = cur.get_prox()

    aux.color[u] = Color.BLACK

    time += 1
    aux.f[u] = time
    return time


def DFS(G: Graph):
    aux = DFSAuxiliar(G.vertexes)

    for u in G.vertexes:
        if aux.color[u] == Color.WHITE:
            time = 0
            aux.c_root = u
            time = DFS_VISIT(G, aux, u, time)

    # print(aux.r)
    # print(aux.d)
    # print(aux.f)
    return aux
