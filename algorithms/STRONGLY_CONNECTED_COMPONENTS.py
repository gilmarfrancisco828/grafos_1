# from collections import defaultdict
# from structs.adj_list import AdjList
# from structs.adj_mat import AdjMatrix
from structs.graph import Graph
from algorithms.DFS import *
from algorithms.TRANSPOSE import *
from algorithms.PRINT_GRAPH import *
from algorithms.MINIMUM_PATH_AOG import *
import random

def transpose(G: Graph):
    Gt = AdjMatrix(G.get_len(), G.get_type(), G.is_valued())
    for u in G.vertexes:
        for v in G.vertexes[u]:
            if Gt.is_valued():
                Gt.make_relation(v, u, G.get_value(u, v))
            else:
                Gt.make_relation(v, u)
    return Gt


def STRONGLY_CONNECTED_COMPONENTS(G: Graph):
    order = TOPOLOGICAL_SORT(G)
    Gt = transpose(G)
    order.reverse()

    # print(order)
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(25,15))
    # ax = axes.flatten()

    # print(sorted(G.vertexes))
    print(sorted(Gt.vertexes))
    res = DFS(Gt, all=True, order=order)
    random.seed()
    roots = set()
    for v in res.r:
        roots.add(res.r[v])
    hex_colors = {}
    r = lambda: random.randint(0, 255)
    for i in roots:
        hex_colors[i] = '#%02X%02X%02X' % (r(), r(), r())
    # print(hex_colors)
    # print(res.r)
    colors = {
        'roots': roots,
        'hex': hex_colors,
        'elements': res.r
    }
    print(roots)
    print(res.r)
    PRINT_GRAPH(G, axes, 'Componentes Fortemente Conexas', colors=colors)
    # PRINT_GRAPH(Gt, ax[1], 'Transposto')
    plt.show() # display
    return roots, res.r