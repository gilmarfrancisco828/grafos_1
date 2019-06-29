from test.helper_leitura import *
from algorithms.PRINT_GRAPH import *
from algorithms.MINIMUM_PATH_AOG import *
from structs.graph import Type


if __name__ == "__main__":
    # main()
    contents = read_file("test/test_files/17_topological.txt")
    graph = generate_graph(contents, False, False, False)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 15))
    PRINT_GRAPH(graph, axes[0], "Grafo", colors=None, colors_fun=get_colors_tree)
    
    order = TOPOLOGICAL_SORT(graph)
    edges= []
    order.reverse()
    # print(order)
    graph_caminho = AdjMatrix(graph.get_len(), Type.DIGRAPH, False)
    ant = order.pop(0)
    for v in order:
        edges.append((ant, v))
        graph_caminho.make_relation(ant, v)
        ant = v

    PRINT_GRAPH(graph_caminho, axes[1], "Ordem Topológica", colors=edges, colors_fun=get_colors_bfs)
    plt.show() # display