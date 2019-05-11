from graph import Graph


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
    def __init__(self, s: int, len: int):
        self.Q = MinHeap()
        self.d = [float('inf') for i in range(0, len)]
        self.pi = [None for i in range(0, len)]
        self.d[s] = 0
        self.Q.updateKey((0, 0))


def relax(aux: DijkstraAux, u: int, v: int, w: int):
    if aux.d[v] > (aux.d[u]+w):
        aux.d[v] = aux.d[u] + w
        aux.pi[v] = u
        aux.Q.updateKey((aux.d[u] + w, v))
        print((aux.d[u] + w, u))



def DIJKSTRA_LIST(G: Graph, s):
    aux = DijkstraAux(s, G.len)
    S = []
    
    while len(aux.Q.heap) != 0:
        # print("Len:",len(aux.Q.heap))
        u = aux.Q.extractMin()[1]
        # print("u:", u)
        S.append(u)
        current = G.vertices[u]
        if isinstance(G, AdjMatrix):
            while current is not None:
                relax(aux, u, current.get_val(), current.get_depth())
                current = current.get_prox()
            # break
        elif isinstance(G, AdjMatrix):
            for v in G.vertexes[u]:
                relax(aux, u, current.get_val(), current.get_depth())
        else:
            print('Erro: Formato inválido!')

    print(aux.d)
    print(aux.pi)


print(DIJKSTRA_LIST(graph, 0))

