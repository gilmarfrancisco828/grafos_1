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

    def __init__(self, vertexes, s):
        # self.path = True if s is not None else False
        self.color = defaultdict(dict)
        self.d = defaultdict(dict)
        # self.f = defaultdict(dict)
        # self.r = defaultdict(dict)
        self.order = []
        # if self.path:
        #     self.pi = defaultdict(dict)

        for i in vertexes:
            self.color[i] = Color.WHITE
            self.d[i] = float('inf')
            # self.f[i] = float('inf')
            # if self.path:
                # self.pi[i] = None


def DFS_VISIT(G: Graph, aux: DFSAuxiliar, u):
    aux.color[u] = Color.GRAY
    if isinstance(G, AdjMatrix):
        for v in G.vertexes[u]:
            if (aux.color[v] == Color.WHITE):
                DFS_VISIT(G, aux, v)
    else:
        cur = G.vertexes[u]
        while cur is not None:
            if aux.color[cur.get_index()] == Color.WHITE:
                DFS_VISIT(G, aux, cur.get_index())
            cur = cur.get_next()

    aux.color[u] = Color.BLACK
    aux.order.append(u)


class TopologicalAux(object):
    
    def __init__(self, G: Graph, s):
        self.d = defaultdict(dict)
        self.pi = defaultdict(dict)

        for i in G.vertexes:
            self.d[i] = float('inf')
            self.pi[i] = None
        if s in G.vertexes:
            self.d[s] = 0


def TOPOLOGICAL_SORT(G: Graph, s=None):
    """Executa a DFS e retorna uma pilha
    """
    aux = DFSAuxiliar(G.vertexes, s)

    if s is not None and s not in G.vertexes:
        return aux.order

    if s is not None:
        aux.c_root = s
        DFS_VISIT(G, aux, s)

    if s is None:
        for u in G.vertexes:
            if aux.color[u] == Color.WHITE:
                DFS_VISIT(G, aux, u)

    return aux.order


def relax(aux: TopologicalAux, u, v, w: int):
    if aux.d[v] > (aux.d[u]+w):
        aux.d[v] = aux.d[u] + w
        aux.pi[v] = u


def MINIMUM_PATH_AOG(G, s):
    k = TOPOLOGICAL_SORT(G, s)
    aux = TopologicalAux(G, s)
    for u in k:
        if isinstance(G, AdjMatrix):
            for v in G.vertexes[u]:
                relax(aux, u, v, G.get_value(u, v))
        else:
            cur = G.vertexes[u]
            while cur is not None:
                relax(aux, u, cur.get_index(), cur.get_value())
                cur = cur.get_next()
    return aux
