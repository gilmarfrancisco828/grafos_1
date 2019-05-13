from algorithms.KRUSKAL import *
from structs.graph import Type


def res(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor X")

def tests():
    print("+++ Testes para Kruskal +++++++++++++++++++++++++++++++")
    # grafo vazio
    contents = read_file("test/test_files/01_vazio.txt")
    graph = generate_graph(contents, True, True)
    result = KRUSKAL(graph)
    print("- Teste para Dígrafo Vazio")
    res(not(len(result)))

    # grafo unitário
    contents = read_file("test/test_files/02_unitario.txt")
    graph = generate_graph(contents, True, True)
    result = KRUSKAL(graph)
    print("- Teste para Dígrafo Unitário")
    res(not(len(result)))

    # grafo com 3 vertices e um loop
    contents = read_file("test/test_files/03_3vertices_1loop.txt")
    graph = generate_graph(contents, True, True)
    result = KRUSKAL(graph)
    print("- Teste para Dígrafo com 3 Vértices e 1 Loop positivo")
    res(result == [('a', 'b'), ('b', 'c')])

    # # grafo nao conexo
    contents = read_file("test/test_files/04_nao_conexo.txt")
    graph = generate_graph(contents, True, True)
    result = KRUSKAL(graph)
    print("- Teste para Dígrafo Não Conexo")
    res(result == [])
    
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
