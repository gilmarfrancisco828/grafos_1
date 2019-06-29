from structs.graph import Graph
from collections import defaultdict
from heapq  import heappop, heappush
from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix
from app.print_path_bellman_ford import *


class MinHeap:
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)/2

    # Inserts a new key 'k'
    def updateKey(self, k):
        heappush(self.heap, k)

    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i][0] = new_val
        while(i != 0 and self.heap[self.parent(i)][0] > self.heap[i][0]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)], self.heap[i])

    # Method to remove minium element from min heap
    def extractMin(self):
        return heappop(self.heap)

    # This functon deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]


class DijkstraAux(object):

    def __init__(self, s, len: int, len_edge: int):
        self.Q = MinHeap()
        # self.d = [float('inf') for i in range(0, len)]
        # self.pi = [None for i in range(0, len)]
        self.d = defaultdict(dict)
        self.pi = defaultdict(dict)
        self.Q.updateKey((0, s))
        self.max_it = len + len_edge
        self.loop = 0

    def print_dijkstra(self, s):
        print_path(self, s)
    
    def get_path(self, u):
        path = []
        if self.pi[u] is None:
            return []
        else:
            inc = u
            len = self.d[inc]
            # print(self.d[inc])
            # input()
            while self.pi[inc] is not None: 
                path.append((self.pi[inc], inc))
                inc = self.pi[inc]
                # len += self.d[inc]
        return path
    

def relax(aux: DijkstraAux, u, v, w: int):
    if aux.d[v] > (aux.d[u]+w):
        aux.d[v] = aux.d[u] + w
        aux.pi[v] = u
        aux.Q.updateKey((aux.d[u] + w, v))
        # print((aux.d[u] + w, u))


def DIJKSTRA(G: Graph, s):
    aux = DijkstraAux(s, G.get_len(), G.get_len_edges())
    for i in G.vertexes:
        aux.d[i] = float('inf')
        aux.pi[i] = None

    if s in G.vertexes:
        aux.d[s] = 0
    else:
        return aux

    S = []
    # G.print_all_vertexes()
    while len(aux.Q.heap) != 0 and aux.loop < aux.max_it:
        # print("Len:",len(aux.Q.heap))
        u = aux.Q.extractMin()[1]
        S.append(u)
        current = G.vertexes[u]
        # print(current)
        if isinstance(G, AdjList):
            while current is not None and current != {}:
                relax(aux, u, current.get_index(), current.get_value())
                current = current.get_next()
            # break
        elif isinstance(G, AdjMatrix):
            for v in G.vertexes[u]:
                relax(aux, u, v, G.get_value(u, v))
        else:
            print('Erro: Formato inválido!')
        aux.loop +=1


    # print(aux.d)
    # print(aux.pi)
    return aux

#print(DIJKSTRA_LIST(G, 0))

