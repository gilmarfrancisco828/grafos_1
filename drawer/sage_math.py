# http://anaustralianteacher.blogspot.com/2012/12/see-here-for-how-to-install-sagemath-at.html
import sys
from sage import *

# A = random_matrix(ZZ,6, density=0.5)
G = DiGraph(A, format='weighted_adjacency_matrix')  # graph from matrix
H = G.plot(edge_labels=True, graph_border=True)
H.show()             # display on screen
H.save('graph.pdf')  # save plot to vector pdf for inclusion in a paper