from structs.graph import Graph
from collections import defaultdict
from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix


def PRIM(G: Graph, r):
    """Retorna a árvore geradora mínima de um grafo
    """
    S = {r}
    X = []
    A = []

    if isinstance(G, AdjMatrix):
        for u in G.vertexes:
            for v in G.vertexes[u]:
                A.append((u, v, G.get_value(u, v)))
    else:
        for u in G.vertexes:
            cur = G.vertexes[u]
            while cur is not None:
                A.append((u, cur.get_index(), cur.get_value()))
                cur = cur.get_next()
    
    A_ativos = [True for i in range(0, len(A))]

    # sort the list of vertices
    A = sorted(A, key=lambda x: x[2])
    # for x in A:
        # print("(", x[0]+1,",", x[1]+1, ",", x[2],")", end=';')
    # return
    while len(X) < (G.get_len()-1) and len(A) != 0:
        for i in range(0, len(A)):

            if(A_ativos[i]):
                a = (A[i][0] in S)
                b = (A[i][1] in S)
                if (a + b) == 1:
                    X.append({A[i][0], A[i][1], A[i][2]})
                    if a:
                        S.add(A[i][1])
                    else:
                        S.add(A[i][0])
                    A_ativos[i] = False
                    break
    return X
