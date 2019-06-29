from structs.graph import *
from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix
try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx
# from networkx.drawing.nx_agraph import write_dot, graphviz_layout
color_default = '#8888FF'
color_warning = '#FF8888'

def get_colors_tree(G, pos, axe, colors):
    # print(colors)
    # print(G.edges())
    # exit()
    nx.draw_networkx_edges(G,
        pos=pos, ax=axe, 
        edgelist=colors, width=6, 
        alpha=0.8, edge_color=color_default)
        # connectionstyle='arc3,rad=0.2'
    nx.draw_networkx_nodes(G,pos=pos, node_color=color_default, nodelist=G.nodes(), label='Intermediários')


def get_colors_bfs(G, pos, axe, colors):
    get_colors_tree(G, pos, axe, colors)
    color = []
    # legend = {'Início': color_warning, 'Intermediários': color_default}
    # print(colors[0][0])
    nx.draw_networkx_nodes(G,pos=pos, node_color=color_warning, nodelist=[colors[0][0]], label='Início')
    axe.legend()
    
def get_colors_components(G, pos, axe, colors):
    for i in G.nodes():
        cor = colors['hex'][colors['elements'][i]]
        nx.draw_networkx_nodes(G, pos=pos, node_color=cor, nodelist=i)

    for u, v in G.edges():
        # print(u, v)
        if colors['elements'][u] == colors['elements'][v]:
            nx.drawing.nx_pylab.draw_networkx_edges(G,
                pos=pos, ax=axe, 
                edgelist=[(u, v)], width=6, 
                alpha=0.8, edge_color=colors['hex'][colors['elements'][u]])


def PRINT_GRAPH(graph: Graph, axe=None, title='', colors=None,
                colors_fun=None):

    if graph.get_type() == Type.DIGRAPH:
        G=nx.DiGraph()
    elif graph.get_type() == Type.GRAPH:
        G=nx.Graph()
    G.add_nodes_from(sorted(graph.vertexes))
    for u in graph.vertexes:
        for v in graph.vertexes[u]:
            if graph.is_valued():
                # if color 
                G.add_edge(u, v, weight=graph.get_value(u, v))
            else:
                G.add_edge(u, v)
    # pos=graphviz_layout(G, prog='circo')
    pos=nx.circular_layout(G)
    # chama a funcao de coloracao caso se deseja alterar cores dos grafos
    nx.draw_networkx(G, pos=pos, ax=axe)

    if colors is not None:
        if colors_fun is not None:
            colors_fun(G, pos, axe, colors)

    if graph.is_valued():
        labels = nx.get_edge_attributes(G, 'weight')
        # nx.draw_networkx_edge_labels(G, pos=pos, ax=axe, edge_labels=labels)
        nx.draw_networkx_edge_labels(G, pos=pos, ax=axe, edge_labels=labels)


    if axe is not None:
        axe.set_axis_off()
        axe.title.set_text(title)
    # else:
        # nx.draw_networkx(G, pos=nx.circular_layout(G))
        # nx.draw_circular(G)