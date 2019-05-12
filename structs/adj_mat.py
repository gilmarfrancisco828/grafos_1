from structs.graph import Graph, Type
from collections import defaultdict


class AdjMatrix(Graph):

    def __init__(self, _len: int, _type: Type, _val: bool):
        super().__init__(_len, _type, _val)
        self.vertexes = defaultdict(dict)

    def make_relation(self, a, b, val=1) -> bool:
        if b is None:  # if the vertice has no relations
            self.vertexes[a] = {}
            return True
        
        if a not in self.vertexes:
            self.vertexes[a] = {}
        self.vertexes[a][b] = val

        if b not in self.vertexes:
            self.vertexes[b] = {}
        
        if(self.get_type() == Type.GRAPH):
            self.vertexes[b][a] = val
    
    def is_adjacent(self, a, b) -> bool:
        if a in self.vertexes and b in self.vertexes[a]:
            return True
        else:
            return False

    def get_value(self, a, b):
        if a in self.vertexes and b in self.vertexes[a]:
            return self.vertexes[a][b]
        return None

    def print_all(self):
        for a in self.vertexes:
            for b in self.vertexes[a]:
                if self.is_valued():
                    print("(", a, ",", b, ",", self.get_value(a, b), ")")
                else:
                    print("(", a, ",", b, ")")

