from collections import defaultdict
from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix
from structs.graph import Graph


def KRUSKAL(G: Graph):
    """Retorna a árvore geradora mínima de um grafo
    """
    Al = []
    X = []
    setV = defaultdict(dict)
    # get all the edges
    for u in G.vertexes:
        setV[u] = u
        if isinstance(G, AdjList):
            cur = G.vertexes[u]

            while cur is not None:
                Al.append((u, cur.get_index(), cur.get_value()))
                cur = cur.get_next()
        else:
            for v in G.vertexes[u]:
                Al.append((u, v, G.get_value(u, v)))

    # sort the list of vertices
    Al = sorted(Al, key=lambda x: x[2])
    for uv in Al:
        u = setV[uv[0]]
        v = setV[uv[1]]
        if u != v:
            X.append((uv[0], uv[1]))
            for i in setV:
                if setV[i] == v:
                    setV[i] = u
    return X
