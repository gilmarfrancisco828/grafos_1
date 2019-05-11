from algorithms.DFS import *
from structs.graph import Type


def res_cor(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor de cores")


def res_d(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor d")


def res_f(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor f")


def tests():
    print("+++ Testes para DFS +++++++++++++++++++++++++++++++")
    # grafo vazio
    contents = read_file("test/test_files/01_vazio.txt")
    graph = generate_graph(contents, True, True)
    result = DFS(graph, '0')
    print("- Teste para Grafo Vazio")
    res_cor(not(len(result.color)))
    res_d(not(len(result.d)))
    res_f(not(len(result.f)))

    # grafo unitário
    contents = read_file("test/test_files/02_unitario.txt")
    graph = generate_graph(contents, True, True)
    result = DFS(graph, 'a')
    print("- Teste para Grafo Unitário")
    res_cor(result.color == {'a': Color.BLACK})
    res_d(result.d == {'a': 1})
    res_f(result.f == {'a': 2})

    # grafo com 4 vertices e um loop
    contents = read_file("test/test_files/03_3vertices_1loop.txt")
    graph = generate_graph(contents, True, True)
    result = DFS(graph, 'a')
    print("- Teste para Grafo 3 Vértices e 1 Loop")
    res_cor(result.color == {'a': Color.BLACK, 'b': Color.BLACK, 'c': Color.BLACK})
    res_d(result.d == {'a': 1, 'b': 2, 'c': 3})
    res_f(result.f == {'a': 6, 'b': 5, 'c': 4})

    # grafo nao conexo
    contents = read_file("test/test_files/04_nao_conexo.txt")
    graph = generate_graph(contents, True, True)
    result = DFS(graph, 'a')
    print("- Teste para Grafo Não Conexo")
    res_cor(result.color == {'a': Color.BLACK, 'b': Color.WHITE})
    res_d(result.d == {'a': 1, 'b': float('inf')})
    res_f(result.f == {'a': 2, 'b': float('inf')})

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")

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
    main()
