from algorithms.DFS import *
from structs.graph import Type

def print_times(aux: DFSAuxiliar):
    for v in aux.color:
        print('', v, '=> Chegada:', aux.d[v], '\tFinalização:', aux.f[v])

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
    print_times(DFS(graph, input('start:')))
