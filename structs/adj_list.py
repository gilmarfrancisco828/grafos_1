from structs.graph import Graph, Type


class Item():
    def __init__(self, index):
        self.index = index
        self.next = None

    def get_index(self):
        return self.index

    def set_next(self, next):
        self.next = next

    def get_next(self):  # -> Item: nao pode usar pq ainda se esta definindo o Item aqui (provavelmente)
        return self.next


class ValItem(Item):
    def __init__(self, index, val: int):
        super().__init__(index)
        self.val = val

    def get_value(self) -> int:
        return self.val

class AdjList(Graph):

    def __init__(self, _len: int, _type: Type, _val: bool):
        super().__init__(_len, _type, _val)


    def make_relation(self, a, b=None, val=1) -> bool:
        if b is None:  # if the vertice has no relations
            self.vertexes[a] = None
            return True

        if a not in self.vertexes or self.vertexes[a] is None:
            if self.is_valued():
                self.vertexes[a] = ValItem(b, val)
            else:
                self.vertexes[a] = Item(b)
        else:
            cur = self.vertexes[a]
            while cur.get_next() is not None:
                if cur.get_index() == b:  # não pode ter relação múltipla???
                    return False
                cur = cur.get_next()
            if self.is_valued():
                cur.set_next(ValItem(b, val))
            else:
                cur.set_next(Item(b))
        
        if b not in self.vertexes:
            self.vertexes[b] = None

        if(self.get_type() == Type.GRAPH):
            if b not in self.vertexes or self.vertexes[b] is None:
                if self.is_valued():
                    self.vertexes[b] = ValItem(a, val)
                else:
                    self.vertexes[b] = Item(a)
            else:
                cur = self.vertexes[b]
                while cur.get_next() is not None:
                    if cur.get_index() == a:
                        return False
                    cur = cur.get_next()
                if self.is_valued():
                    cur.set_next(ValItem(a, val))
                else:
                    cur.set_next(Item(a))

    def is_adjacent(self, a, b) -> bool:
        cur = self.vertexes[a]
        while cur is not None:
            if cur.get_index() == b:
                return True
            cur = cur.get_next()
        return False

    def get_value(self, a, b):
        if self.is_valued():
            if a in self.vertexes:
                cur = self.vertexes[a]
                while cur is not None:
                    if b == cur.get_index():
                        return cur.get_value()
                    cur = cur.get_next()
        return None

    def print_all(self):
        for a in self.vertexes:
            cur = self.vertexes[a]
            while cur is not None:
                if self.is_valued():
                    print("(", a, ",", cur.get_index(), ",", cur.get_value(), ")")
                else:
                    print("(", a, "," + cur.get_index(), ")")
                cur = cur.get_next()

    def print_all_vertexes(self):
        print('Vértices: ', end='')
        for x in self.vertexes:
            print(x, end=' ')
        print()
        
    def get_len(self):
        return self._len