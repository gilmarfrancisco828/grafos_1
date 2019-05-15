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
        self.path = True if s is not None else False
        self.color = defaultdict(dict)
        self.d = defaultdict(dict)
        self.f = defaultdict(dict)
        self.r = defaultdict(dict)
        if self.path:
            self.pi = defaultdict(dict)

        for i in vertexes:
            self.color[i] = Color.WHITE
            self.d[i] = float('inf')
            self.f[i] = float('inf')
            if self.path:
                self.pi[i] = None

    def print_DFS(self):
        print('Descoberta: ', self.d)
        print('Finalização: ', self.f)


def DFS_VISIT(G: Graph, aux: DFSAuxiliar, u, time: int):
    aux.color[u] = Color.GRAY
    time += 1
    aux.d[u] = time
    aux.r[aux.c_root] = u  # labels the vertexes
    if isinstance(G, AdjMatrix):
        for v in G.vertexes[u]:
            if (aux.color[v] == Color.WHITE):
                if aux.path:
                    aux.pi[v] = u
                time = DFS_VISIT(G, aux, v, time)
    else:
        cur = G.vertexes[u]
        while cur is not None:
            if aux.color[cur.get_index()] == Color.WHITE:
                if aux.path:
                    aux.pi[cur.get_index()] = u
                time = DFS_VISIT(G, aux, cur.get_index(), time)
            cur = cur.get_next()

    aux.color[u] = Color.BLACK

    time += 1
    aux.f[u] = time
    return time


def DFS(G: Graph, s=None, all=False):
    """Executa a DFS
    s: configura o vertice inicial, por onde a busca comeca
    caso seja None a funcao passa por todos
        - Caso o s seja passado a DFS também salva vetor pi
    all: configura se mesmo com um vertice inicial ainda se
    quer que a funcao percorra todos os vertices
    """
    aux = DFSAuxiliar(G.vertexes, s)
    time = 0

    if s is not None and s not in G.vertexes:
        return aux

    if s is not None:
        aux.c_root = s
        time = DFS_VISIT(G, aux, s, 0)
    
    # Faz o DFS_VISIT para todos os vertices nos casos:
    # all for True(forcar percorrer por todos) ou
    # s e all nao forem passados por parametro => percorre todos
    if all | (s is None and not all):
        for u in G.vertexes:
            if aux.color[u] == Color.WHITE:
                aux.c_root = u
                time = DFS_VISIT(G, aux, u, time)

    return aux
