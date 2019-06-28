from algorithms.PRINT_GRAPH import *
from algorithms.STRONGLY_CONNECTED_COMPONENTS import *
from test.helper_leitura import *

contents = read_file("test/test_files/13_componentes.txt")
# ax = axes.flatten()
graph = generate_graph(contents, False, False, False)
# print(graph.vertexes)
# print(res.f)
colors, elements = STRONGLY_CONNECTED_COMPONENTS(graph) 
# print(res.color)
# print(res.d)
# print(res.path)
