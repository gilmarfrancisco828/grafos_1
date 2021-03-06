from algorithms.PRINT_GRAPH import *
from algorithms.DIJKSTRA import *
from structs.graph import Type



def res_d(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor d")


def res_pi(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor pi")

def res_loops(condition):
    print("\t", "✗ " if not(condition) else "✓", "loops")


def tests():
    print("+++ Testes para Dijkstra +++++++++++++++++++++++++++++++")
    # grafo vazio
    contents = read_file("test/test_files/01_vazio.txt")
    graph = generate_graph(contents, True, True)
    graph.set_num_edges(get_len_edges(contents))
    result = DIJKSTRA(graph, '0')
    print("- Teste para Grafo Vazio")
    res_d(not(len(result.d)))
    res_pi(not(len(result.pi)))

    # # grafo unitário
    contents = read_file("test/test_files/02_unitario.txt")
    graph = generate_graph(contents, True, True)
    graph.set_num_edges(get_len_edges(contents))
    result = DIJKSTRA(graph, 'a')
    print("- Teste para Grafo Unitário")
    res_d(result.d == {'a': 0})
    res_pi(result.pi == {'a': None})

    # # grafo nao conexo
    contents = read_file("test/test_files/04_nao_conexo.txt")
    graph = generate_graph(contents, True, True)
    graph.set_num_edges(get_len_edges(contents))
    result = DIJKSTRA(graph, 'a')
    print("- Teste para Grafo Não Conexo")
    res_d(result.d == {'a': 0, 'b': float('inf')})
    res_pi(result.pi == {'a': None, 'b': None})

    # #grafo com loop negativo
    contents = read_file('test/test_files/09_3vertices_1loop_negativo.txt')
    graph = generate_graph(contents, True, True)
    graph.set_num_edges(get_len_edges(contents))
    result = DIJKSTRA(graph, 'a')
    print("- Teste para com Loop negativo")
    res_loops(result.loop < result.max_it)

    contents = read_file('grafo1')
    graph = generate_graph(contents, True, False)
    graph.set_num_edges(get_len_edges(contents))
    result = DIJKSTRA(graph, 's')
    print("- Teste Slide")
    res_d(result.d == {'s': 0, 't': 8, 'x': 9, 'y': 5, 'z': 7})
    res_pi(result.pi == {'s': None, 't': 'y', 'x': 't', 'y': 's', 'z': 'y'})

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")

def read_file(fileName):
    '''Realiza a leitura do arquivo texto que contem 
    o grafo, recebe nome do arquivo'''
    f = open(fileName, "r")
    contents = f.read().split("\n")
    return contents

def get_len_edges(contents):
    return len(contents)-2

def generate_graph(contents: list, val: bool, t_struct: bool):
    """Função recebe uma lista de arestas e cria o grafo
        t_struct: True => AdjList e False => AdjMat
    """
    if t_struct:
        graph = AdjList(int(contents[1]), Type.DIGRAPH, val)
    else:
        graph = AdjMatrix(int(contents[1]), Type.DIGRAPH, val)
    for x in contents[2:]:
        x = x.split()
        if(len(x) == 1):
            graph.make_relation(x[0])
        elif(len(x) == 2):
            graph.make_relation(x[0], x[1])
        else:
            graph.make_relation(x[0], x[1], int(x[2]))

    # graph.print_all()
    return graph

def main():
    tests()


if __name__ == "__main__":
    # main()
    contents = read_file("test/test_files/10_dijkstra.txt")
    graph = generate_graph(contents, True, False)
    graph.set_num_edges(get_len_edges(contents))
    start = 't'
    result = DIJKSTRA(graph, start)
    edges = []
    textstr = 'Distâncias Mínimas:'
    for v in graph.vertexes:
        if v != start:
            soma = 0
            path = result.get_path(v)
            for u, w in path:
                soma += graph.get_value(u, w)
            textstr += "\n{}: {}".format(v, soma)
            edges += path
    print(soma)

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(25, 15))
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    axes.text(0.05, 0.95, textstr, transform=axes.transAxes, fontsize=14, verticalalignment='top', bbox=props)

    PRINT_GRAPH(graph, axes, "Caminho Mínimo - Dijkstra - Início({})".format(start), colors=edges, colors_fun=get_colors_dij)
    plt.show() # display