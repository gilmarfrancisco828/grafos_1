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
        self.color = defaultdict(dict)
        self.d = defaultdict(dict)
        self.f = defaultdict(dict)
        self.r = defaultdict(dict)
        for i in vertexes:
            self.color[i] = Color.WHITE
            self.d[i] = float('inf')
            self.f[i] = float('inf')

    def print_DFS(self):
        print('Descoberta: ', self.d)
        print('Finalização: ', self.f)


def DFS_VISIT(G: Graph, aux: DFSAuxiliar, u, time: int):
    aux.color[u] = Color.GRAY
    time += 1
    aux.d[u] = time
    aux.r[aux.c_root] = u  # labels the vertexes
    print("cheguei")
    if isinstance(G, AdjMatrix):
        for v in G.vertexes[u]:
            if (G.vertexes[u][v] == 1) & (aux.color[v] == Color.WHITE):
                time = DFS_VISIT(G, aux, v, time)
    else:
        cur = G.vertexes[u]
        while cur is not None:
            if aux.color[cur.get_index()] == Color.WHITE:
                time = DFS_VISIT(G, aux, cur.get_index(), time)
            cur = cur.get_next()

    aux.color[u] = Color.BLACK

    time += 1
    aux.f[u] = time
    return time


def DFS(G: Graph, s=None):
    aux = DFSAuxiliar(G.vertexes)

    if s is None:
        for u in G.vertexes:
            if aux.color[u] == Color.WHITE:
                time = 0
                aux.c_root = u
                time = DFS_VISIT(G, aux, u, time)
    else:
        if s not in G.vertexes:
            return aux

        aux.c_root = s
        DFS_VISIT(G, aux, s, 0)

    
    # print(aux.r)
    # print(aux.d)
    # print(aux.f)

    return aux
    

