from structs.graph import Graph
from algorithms.DFS import *
from algorithms.PRINT_GRAPH import *
import random

def connected_components(G: Graph):
    res = DFS(G)
    random.seed()

    r = lambda: random.randint(0, 255)
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(25,15))

    roots = set()
    for v in res.r:
        roots.add(res.r[v])
    hex_colors = {}
    for i in roots:
        hex_colors[i] = '#%02X%02X%02X' % (r(), r(), r())
    colors = {
        'roots': roots,
        'hex': hex_colors,
        'elements': res.r
    }
    

    PRINT_GRAPH(G, axes,'Componentes Conexas',  colors=colors,colors_fun=get_colors_components)
    plt.show()
    return roots, res.r
