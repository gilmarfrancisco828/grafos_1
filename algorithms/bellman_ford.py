from collections import defaultdict
from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix
from structs.graph import Graph


class BellmanFordAux(object):
    def __init__(self, G: Graph, s):
        self.d = defaultdict(dict)
        self.pi = None
        for i in G.vertexes:
            self.d[i] = float('inf')
            self.pi[i] = None
        self.d[s] = 0


def relax(aux: BellmanFordAux, u, v, w: int):
    if aux.d[v] > (aux.d[u]+w):
        aux.d[v] = aux.d[u] + w
        aux.pi[v] = u


def BELLMAN_FORD(G: Graph, s):
    aux = BellmanFordAux(G, s)

    for u in G.vertexes:
        if isinstance(G, AdjMatrix):
            for v in G.vertexes[u]:
                relax(aux, u, v, G.get_value(u, v))
        else:
            cur = G.vertexes[u]
            while cur is not None:
                relax(aux, u, cur.get_index(), cur.get_val())
                cur = cur.get_prox()

    for u in G.vertexes:
        cur = G.vertexes[u]
        while cur is not None:
            if aux.d[cur.get_index()] > (aux.d[u] + cur.get_val()):
                return False
            cur = cur.get_prox()

    return True

