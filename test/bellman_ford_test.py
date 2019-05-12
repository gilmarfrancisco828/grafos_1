from algorithms.bellman_ford import *
from structs.graph import Type


def res_d(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor d")


def res_pi(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor pi")

def res_negativo(condition):
    print ("\t", "✗" if (condition) else "✓", "Retornou False em Loop negativo")


def tests():
    print("+++ Testes para Bellman Ford +++++++++++++++++++++++++++++++")
    # grafo vazio
    contents = read_file("test/test_files/01_vazio.txt")
    graph = generate_graph(contents, True, True)
    result = BELLMAN_FORD(graph, '0')[1]
    print(result.d)
    print("- Teste para Dígrafo Vazio")
    res_d(not(len(result.d)))
    res_pi(not(len(result.pi)))

    # grafo unitário
    contents = read_file("test/test_files/02_unitario.txt")
    graph = generate_graph(contents, True, True)
    result = BELLMAN_FORD(graph, 'a')[1]
    print("- Teste para Dígrafo Unitário")
    res_d(result.d == {'a': 0})
    res_pi(result.pi == {'a': None})

    # grafo com 3 vertices e um loop
    contents = read_file("test/test_files/03_3vertices_1loop.txt")
    graph = generate_graph(contents, True, True)
    result = BELLMAN_FORD(graph, 'a')[1]
    print("- Teste para Dígrafo com 3 Vértices e 1 Loop positivo")
    res_d(result.d == {'a': 0, 'b': 1, 'c': 3})
    res_pi(result.pi == {'a': None, 'b': 'a', 'c': 'a'})

    # grafo com 3 vertices e um loop negativo
    contents = read_file("test/test_files/09_3vertices_1loop_negativo.txt")
    graph = generate_graph(contents, True, True)
    result = BELLMAN_FORD(graph, 'a')
    print("- Teste para Dígrafo com 3 Vértices e 1 Loop negativo")
    res_negativo(result[0])
    res_d(result[1].d == {'a': 0, 'b': -1, 'c': -3})
    res_pi(result[1].pi == {'a': None, 'b': 'a', 'c': 'b'})

    # grafo nao conexo
    contents = read_file("test/test_files/04_nao_conexo.txt")
    graph = generate_graph(contents, True, True)
    result = BELLMAN_FORD(graph, 'a')[1]
    print("- Teste para Dígrafo Não Conexo")
    res_d(result.d == {'a': 0, 'b': float('inf')})
    res_pi(result.pi == {'a': None, 'b': None})

    # grafo exemplo slide
    contents = read_file("test/test_files/09_bellman_ford_slide.txt")
    graph = generate_graph(contents, True, False)
    result = BELLMAN_FORD(graph, 'r')[1]
    print("- Teste exemplo do slide")
    res_d(result.d == {'r': 0, 's': 3, 't': 5, 'u': 4})
    res_pi(result.pi == {'r': None, 's': 'r', 't': 'u', 'u': 's'})

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


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


def main():
    tests()


if __name__ == "__main__":
    main()
