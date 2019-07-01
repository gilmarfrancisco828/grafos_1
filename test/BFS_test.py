from test.helper_leitura import *
from algorithms.PRINT_GRAPH import *
from algorithms.BFS import *
from structs.graph import Type

def res_cor(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor de cores")


def res_d(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor d")


def res_pi(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor pi")


# def tests():
    print("+++ Testes para BFS +++++++++++++++++++++++++++++++")
    # grafo vazio
    contents = read_file("test/test_files/01_vazio.txt")
    # graph = generate_graph(contents, True, True)
    result = BFS(graph, '0')
    print("- Teste para Grafo Vazio")
    res_cor(not(len(result.color)))
    res_d(not(len(result.d)))
    res_pi(not(len(result.pi)))

    # grafo unitário
    contents = read_file("test/test_files/02_unitario.txt")
    # graph = generate_graph(contents, True, True)
    result = BFS(graph, 'a')
    print("- Teste para Grafo Unitário")
    res_cor(result.color == {'a': Color.BLACK})
    res_d(result.d == {'a': 0})
    res_pi(result.pi == {'a': None})

    # grafo com 4 vertices e um loop
    contents = read_file("test/test_files/03_3vertices_1loop.txt")
    # graph = generate_graph(contents, True, True)
    result = BFS(graph, 'a')
    print("- Teste para Grafo 3 Vértices e 1 Loop")
    res_cor(result.color == {'a': Color.BLACK, 'b': Color.BLACK, 'c': Color.BLACK})
    res_d(result.d == {'a': 0, 'b': 1, 'c': 1})
    res_pi(result.pi == {'a': None, 'b': 'a', 'c': 'a'})

    # grafo nao conexo
    contents = read_file("test/test_files/04_nao_conexo.txt")
    # graph = generate_graph(contents, True, True)
    result = BFS(graph, 'a')
    print("- Teste para Grafo Não Conexo")
    res_cor(result.color == {'a': Color.BLACK, 'b': Color.WHITE})
    res_d(result.d == {'a': 0, 'b': float('inf')})
    res_pi(result.pi == {'a': None, 'b': None})

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")

# def read_file(fileName):
#     '''Realiza a leitura do arquivo texto que contem 
#     o grafo, recebe nome do arquivo'''
#     f = open(fileName, "r")
#     contents = f.read().split("\n")
#     return contents


# def generate_graph(contents: list, val: bool, t_struct: bool):
#     """Função recebe uma lista de arestas e cria o grafo
#         t_struct: True => AdjList e False => AdjMat
#     """
#     if t_struct:
#         graph = AdjList(int(contents[1]), Type.GRAPH, val)
#     else:
#         graph = AdjMatrix(int(contents[1]), Type.GRAPH, val)
#     for x in contents[2:]:
#         x = x.split()
#         if(len(x) == 1):
#             graph.make_relation(x[0])
#         elif(len(x) == 2):
#             graph.make_relation(x[0], x[1])
#         else:
#             graph.make_relation(x[0], x[1], int(x[2]))

#     # graph.print_all()
#     return graph


def main():
    # tests()
    pass


if __name__ == "__main__":
    # main()
    contents = read_file("test/test_files/16_BFS.txt")
    graph = generate_graph(contents, False, False, False)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 15))
    PRINT_GRAPH(graph, axes[0], "Grafo", colors=None, colors_fun=get_colors_tree)
        
    result = BFS(graph, 'F')
    edges= []
    order = list(result.q_path.queue)
    # print(order)
    graph_caminho = AdjMatrix(graph.get_len(), Type.DIGRAPH, False)
    ant = order.pop(0)
    for v in order:
        edges.append((ant, v))
        graph_caminho.make_relation(ant, v)
        ant = v

    PRINT_GRAPH(graph_caminho, axes[1], "BFS", colors=edges, colors_fun=get_colors_bfs)
    plt.show() # display