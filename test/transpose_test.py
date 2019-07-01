from algorithms.TRANSPOSE import *
from algorithms.PRINT_GRAPH import *
from test.helper_leitura import *


contents = read_file("test/test_files/11_prim_slide.txt")
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25,15))
ax = axes.flatten()

graph = generate_graph(contents, True, False, False)

print(graph.is_valued())
PRINT_GRAPH(graph, ax[0], 'Original')


grapht = transpose(graph)
PRINT_GRAPH(grapht, ax[1], 'Transposto')
print(graph.vertexes['b'])
plt.show() # display

