from structs.graph import *
from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix
try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout

def PRINT_GRAPH(graph: Graph, axe=None, title='', colors=None):
    color = None
    edges_colors = None
    if graph.get_type() == Type.DIGRAPH:
        G=nx.MultiDiGraph()
    elif graph.get_type() == Type.GRAPH:
        G=nx.Graph()
    for u in sorted(graph.vertexes):
        for v in sorted(graph.vertexes[u]):
            if graph.is_valued():
                # if color 
                G.add_edge(u, v, weight=graph.get_value(u, v))
            else:
                G.add_edge(u, v)
    # pos=graphviz_layout(G, prog='twopi')
    pos=nx.circular_layout(G)

    if colors is not None:
        color = []
        edges_colors = []
        for i in G.nodes():
            color.append(colors['hex'][colors['elements'][i]])
        # print(color)
        for u, v in G.edges():
            # print(u, v)
            if colors['elements'][u] == colors['elements'][v]:
                nx.draw_networkx_edges(G,
                    pos=pos, ax=axe, 
                    edgelist=[(u, v)], width=6, 
                    alpha=0.8, edge_color=colors['hex'][colors['elements'][u]])
                
    if graph.is_valued():
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G, nx.circular_layout(G), ax=axe, edge_labels=labels)
        # nx.draw_networkx_edges(G, nx.circular_layout(G), ax=axe, edge_color=edges_colors)
        # nx.draw_networkx_edges(G, pos=nx.spring_layout(G), axe=axe, )
    nx.draw_networkx(G, pos=pos, ax=axe, node_color=color)

    if axe is not None:
        axe.set_axis_off()
        axe.title.set_text(title)
    # else:
        # nx.draw_networkx(G, pos=nx.circular_layout(G))
        # nx.draw_circular(G)