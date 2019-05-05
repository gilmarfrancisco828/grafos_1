from graph import Graph, Type


class Item():
    def __init__(self, index):
        self.index = index
        self.next = None

    def get_index(self):
        return self.index

    def set_next(self, next):
        self.next = next

    def get_next(self):# -> Item: nao pode usar pq ainda se esta definindo o Item aqui (provavelmente)
        return self.next


class ValItem(Item):
    def __init__(self, index, val: int):
        super(index)

    def get_val(self) -> int:
        return self.val


class AdjList(Graph):

    def __init__(self, _len: int, _type: Type, _val: bool):
        super(_len, _type, _val)
        self.vertexes = {}

    def make_relation(self, a, b, val: int) -> bool:
        if a not in self.vertexes:
            if self.is_valued():
                self.vertexes[a] = ValItem(b, val)
            else:
                self.vertexes[a] = Item(b)
        else:
            current = self.vertexes[a]
            while current.get_next() is not None:
                if current.get_index() == b:
                    return False
                current = current.get_next()
            if self.is_valued():
                current.set_prox(ValItem(b, val))
            else:
                current.set_prox(Item(b))

        if(self.get_type() == Type.GRAPH):
            if b not in self.vertexes:
                if self.is_valued():
                    self.vertexes[b] = ValItem(a, val)
                else:
                    self.vertexes[b] = Item(a)
            else:
                current = self.vertexes[b]
                while current.get_next() is not None:
                    if current.get_index() == a:
                        return False
                    current = current.get_next()
                if self.is_valued():
                    current.set_prox(ValItem(a, val))
                else:
                    current.set_prox(Item(a))

    def is_adjacent(self, a, b) -> bool:
        current = self.vertexes[a]
        while current is not None:
            if current.get_index() == b:
                return True
            current = current.get_next()
        return False

    def print_all(self):
        for vertex in self.vertexes:
            current = self.vertexes[vertex]
            while current is not None:
                if self.is_valued():
                    print("(", vertex, "," + current.get_index(), ",", current.get_val(), ")")
                else:
                    print("(", vertex, "," + current.get_index(), ")")
                current = current.get_prox()
    
    def get_value(self, a, b):
        if self.is_valued():
            if a in self.vertexes:
                current = self.vertices[a]
                while current is not None:
                    if b == current.get_index():
                        return current.get_val()
                    current = current.get_prox()
        return None
