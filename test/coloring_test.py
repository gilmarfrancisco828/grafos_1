from algorithms.COLORING import *
from structs.graph import Type


def res(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor X")

def tests():
    print("+++ Testes para Coloração +++++++++++++++++++++++++++++++")
    # # grafo vazio
    # contents = read_file("test/test_files/01_vazio.txt")
    # graph = generate_graph(contents, False, False, True)
    # result = coloring(graph)
    # print("- Teste para Grafo Vazio")
    # res((result==None))

    # grafo unitário
    # contents = read_file("test/test_files/02_unitario.txt")
    # graph = generate_graph(contents, False, False, True)
    # result = coloring(graph)
    # print("- Teste para Grafo Unitário")
    # # print(result.colored)
    # res((result.colored=={'a':0}))

    # grafo com 6 vertices slide
    contents = read_file("test/test_files/15_coloring_slide.txt")
    graph = generate_graph(contents, False, False, True)
    result = coloring(graph)
    print("- Teste para Grafo com 6 vértices do slide")
    res(result.colored == {'5': 0, '1': 1, '2': 0, '3': 1, '4': 2, '6': 3})

    # # grafo nao conexo
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
    # tests()
    #  python3 - m test.coloring_test
    contents = read_file("test/16_componentes_conectadas_I_grafo.txt")
    contents = read_file("test/16_componentes_conectadas_II_grafo.txt")
    graph = generate_graph(contents, False, False, True)
    result = coloring(graph)

    # contents = read_file("test/test_files/15_coloring_slide.txt")
    # # contents = read_file('test/test_files/03_3vertices_1loop.txt')
    # graph = generate_graph(contents, False, False, True)
    # # graph.print_all()
    # result = coloring(graph)
    # print(result.colored=={'5': 0, '1': 1, '2': 0, '3': 1, '4': 2, '6': 3})
    # # print(result.colored)
    # # for i in graph.vertexes:
    # #     for j in graph.vertexes[i]:
    # #         print(len(graph.vertexes[i]))
    # #         print('i: ', i)
        


if __name__ == "__main__":
    main()
