from algorithms.BFS import *
from structs.graph import Type

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
        graph = AdjList(int(contents[1]), Type.GRAPH, val)
    else:
        graph = AdjMatrix(int(contents[1]), Type.GRAPH, val)
    for x in contents[2:]:
        x = x.split()
        # print(x)
        graph.make_relation(int(x[0]), int(x[1]), int(x[2]))

    # graph.print_all()
    return graph


def main():
    contents = read_file("test/test_files/08_test_final_slide.txt")
    graph = generate_graph(contents, True, True)
    graph.print_all()


if __name__ == "__main__":
    main()
