import algorithms.DIJKSTRA as dijkstra



def res_d(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor d")


def res_pi(condition):
    print ("\t", "✗ " if not(condition) else "✓", "vetor pi")


def tests():
    print("+++ Testes para Dijkstra +++++++++++++++++++++++++++++++")
    # grafo vazio
    contents = read_file("test/test_files/01_vazio.txt")
    graph = generate_graph(contents, True, True)
    result = dijkstra.DIJKSTRA_LIST(graph, '0')
    print("- Teste para Grafo Vazio")
    res_d(not(len(result.d)))
    res_pi(not(len(result.pi)))

    # grafo unitário
    contents = read_file("test/test_files/02_unitario.txt")
    graph = generate_graph(contents, True, True)
    result = dijkstra.DIJKSTRA_LIST(graph, 'a')
    print("- Teste para Grafo Unitário")
    res_d(result.d == {'a': 0})
    res_pi(result.pi == {'a': None})

    

    # grafo nao conexo
    contents = read_file("test/test_files/04_nao_conexo.txt")
    graph = generate_graph(contents, True, True)
    result = dijkstra.DIJKSTRA_LIST(graph, 'a')
    print("- Teste para Grafo Não Conexo")
    res_d(result.d == {'a': 0, 'b': float('inf')})
    res_pi(result.pi == {'a': None, 'b': None})

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
