# from algorithms.PRINT_GRAPH import *

from algorithms.CONNECTED_COMPONENTS import *
from test.helper_leitura import *
# contents = read_file("test/test_files/01_vazio.txt")
# contents = read_file('test/test_files/02_unitario.txt')
contents = read_file("test/16_componentes_conectadas_I_grafo.txt")
# contents = read_file("test/16_componentes_conectadas_II_grafo.txt")
# ax = axes.flatten()
graph = generate_graph(contents, False, False, True)
# graph = generate_graph(contents, True, False, True)
# print(graph.vertexes)
# print(res.f)
res = connected_components(graph) 
# print('pais: ',res.pi)
# print('cors: ',res.color)
# print('d: ',res.d)
# print('f: ',res.f)
# print('r: ',res.r)
print(res)

# print(res.color)
# print(res.d)
# print(res.path)
