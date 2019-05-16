from algorithms.DFS import *
from structs.graph import Type

def is_connected(G: Graph):
    """ Verifica se uma grafo é conexo, caso não seja exibe o
    número de componentes e a qual componente cada vértice
    pertence.
    """
    
    res = DFS(G)
    if len(res.r) > 1:
        print("Grafo não conexo")
        for i in res.r:
            print(i, end=': ')
            print(res.r[i])
    else:
        print("Grafo conexo")

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
    contents = read_file("test/test_files/08_test_final_slide.txt")
    graph = generate_graph(contents, True, False)
    is_connected(graph)