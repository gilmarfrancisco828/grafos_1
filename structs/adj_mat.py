import graph

class AdjMatrix(Graph):

    def __init__(self, _len: int, _type: Type, _val: bool):
        super(_len, _type, _val)
        self.vertexes = {}

    def make_relation(self, a, b, val=1) -> bool:
        if a in not self.vertexes:
            self.vertexes[a] = {}
        self.vertexes[a][b] = val

        if(self.get_type() == Type.GRAPH):
            if b in not self.vertexes:
                self.vertexes[b] = {}
            self.vertexes[b][a] = val
    
    def is_adjacent(self, a, b) -> bool:
        if a in self.vertexes and b in self.vertexes[a]:
            return True
        else:
            return False

    def print_all(self):
        for vertex in self.vertexes:
            for edge in self.vertexes[vertex]:
                if self.is_valued():
                    print("(", vertex, ",", edge, ",", get_value(vertex, edge), ")")
                else:
                    print("(", vertex, ",", edge, ")")
    
    def get_value(self, a, b):
        if a in self.vertexes and b in self.vertexes[a]:
            return self.vertexes[a][b]
        return None
