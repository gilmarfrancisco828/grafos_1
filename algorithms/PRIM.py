from structs.graph import Graph
from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix
import heapq


def prim(G: Graph, r):
    X = []
    chave = {}
    pi = {}
    w = lambda a,b: G.get_value(a,b)
    for u in G.vertexes:
        chave[u] = float('inf')
        pi[u]    = None    
    
    chave[s] = 0
    Q = heapq()
    
    for u in G.vertexes:
        heapq.heappush(Q, chave[u], u)
        
    while Q:
        u = heapq.heappop(Q)
        if u is not r:
            X.append((u, pi[u]))
        if isinstance(G, AdjMatrix):
            for v in G.vertexes[u]:
                if v in Q and w(u,v) < chave[v]:
                    chave[v] = w(u,v)
                    pi[v] = u
        elif isinstance(G, AdjList):
            for v in u.vertexes:
                if v in Q and w(u,v) < chave[v]:
                    chave[v] = w(u,v)
                    pi[v] = u
    return X
        


        


        

    