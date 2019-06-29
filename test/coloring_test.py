from algorithms.COLORING import *
from structs.graph import Type


def res(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor X")

def tests():
    print("+++ Testes para Coloração +++++++++++++++++++++++++++++++")
    # grafo vazio
    contents = read_file("test/test_files/01_vazio.txt")
    graph = generate_graph(contents, False, True, True)
    result = coloring(graph)
    print("- Teste para Grafo Vazio")
    res((result==None))

    # grafo unitário
    contents = read_file("test/test_files/02_unitario.txt")
    graph = generate_graph(contents, False, True, True)
    result = coloring(graph)
    print("- Teste para Grafo Unitário")
    print(result.cc)
    res((result.cc==1))

    # grafo com 6 vertices slide
    contents = read_file("test/test_files/15_coloring_slide.txt")
    graph = generate_graph(contents, False, True, True)
    result = coloring(graph)
    print("- Teste para Grafo com 6 vértices do slide")
    #res(result == [('a', 'b'), ('b', 'c')])

    # # # grafo nao conexo
    # contents = read_file("test/test_files/04_nao_conexo.txt")
    # graph = generate_graph(contents, False, True, True)
    # result = coloring(graph)
    # print("- Teste para Grafo Não Conexo")
    # #res(result == [])
    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def read_file(fileName):
    '''Realiza a leitura do arquivo texto que contem 
    o grafo, recebe nome do arquivo'''
    f = open(fileName, "r")
    contents = f.read().split("\n")
    return contents

def generate_graph(contents: list, val: bool, t_struct: bool, is_graph: bool):
    """Função recebe uma lista de arestas e cria o grafo
        t_struct: True => AdjList e False => AdjMat
    """
    if is_graph:
        _type = Type.GRAPH
    else:
         _type = Type.DIGRAPH

    if t_struct:
        graph = AdjList(int(contents[1]), _type, val)
    else:
        graph = AdjMatrix(int(contents[1]), _type, val)
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


# def generate_graph(contents: list, val: bool, t_struct: bool):
#     """Função recebe uma lista de arestas e cria o grafo
#         t_struct: True => AdjList e False => AdjMat
#     """
#     if t_struct:
#         graph = AdjList(int(contents[1]), Type.DIGRAPH, val)
#     else:
#         graph = AdjMatrix(int(contents[1]), Type.DIGRAPH, val)
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
    tests()


if __name__ == "__main__":
    main()
