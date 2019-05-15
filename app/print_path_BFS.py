from algorithms.BFS import *
from structs.graph import Type


def print_path(result, s):
    for u in result.d:
        print("Vértice:", u)

        if res.pi[u] is None and u == s:
            print("Caminho: Raiz", end='')
        else:
            if result.pi[u] is None:
                print("Não são conectados", end='')
            else:
                print("Caminho:", u, end='')
                inc = u
                len = result.d[inc]
                while result.pi[inc] is not None:
                    print(" > " + str(result.pi[inc]), end='')
                    inc = result.pi[inc]
                    len += result.d[inc]
                print("\n\tDistância:", len, end='')
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
    contents = read_file("test/test_files/08_test_final_slide.txt")
    graph = generate_graph(contents, True, False)
    s = input('start:')
    res = BFS(graph, s)
    # print(res.d)
    print_path(res, s)
