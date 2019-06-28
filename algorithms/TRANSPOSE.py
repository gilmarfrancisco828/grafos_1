from structs.graph import Graph
from algorithms.DFS import *
from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix


def transpose(G: Graph):
    Gt = AdjMatrix(G.get_len(), G.get_type(), G.is_valued())
    for u in G.vertexes:
        for v in G.vertexes[u]:
            if Gt.is_valued():
                Gt.make_relation(v, u, G.get_value(u, v))
    return Gt