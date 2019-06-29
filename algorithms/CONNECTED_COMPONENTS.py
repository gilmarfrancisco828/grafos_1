from structs.graph import Graph
from algorithms.DFS import *



def connected_components(G: Graph):
    res = DFS(G)
    roots = set()
    for v in res.r:
        roots.add(res.r[v])
    return roots, res.r
