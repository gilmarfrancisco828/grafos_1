from algorithms.bellman_ford import *
from algorithms.DIJKSTRA import *
from structs.graph import Type
# Funcion to print the path from a vertex to another one
def print_path(result, vertex):
    if result.pi[vertex] is None:
        print("Não são conectados", end='')
        return

    print("Caminho:", vertex, end='')
    inc = vertex
    while result.pi[inc] is not None:
        print(" > " + str(result.pi[inc]), end='')
        inc = result.pi[inc]


# Funcion to print the path to an especific graph
def minimum_path(func, G: Graph, s):
    """Recebe as estruturas auxiliares do algoritmo e exibe
        o caminho para chegar em cada vértice
    """

    if func is BELLMAN_FORD:
        res = func(G, s)[1]
    else:
        res = func(G, s)

    print("")

    for u in G.vertexes:
        print("Vértice:", u)

        if res.pi[u] is None and u == s:
            print("Caminho: Raiz", end='')
        else:
            print_path(res, u)

        print("\n")


def read_file(fileName):
    '''Realiza a leitura do arquivo texto que contem 
    o grafo, recebe nome do arquivo'''
    f = open(fileName, "r")
    contents = f.read().split("\n")
    return contents

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


if __name__ == "__main__":
    contents = read_file("test/test_files/09_bellman_ford_slide.txt")
    graph = generate_graph(contents, True, False)
    minimum_path(BELLMAN_FORD, graph, 'u')