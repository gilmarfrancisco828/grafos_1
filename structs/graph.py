class Type(Enum):
    GRAPH = False
    DIGRAPH = True

class Graph(object):

    def __init__(self, _len: int, _type: Type, _val: bool):
        self._len = _len
        self._type = _type
        self._val = _val
    
    @abstractmethod
    def make_relation(self, a, b, val: int) -> bool:
        pass
    
    @abstractmethod
    def is_adjacent(self, a, b) -> bool:
        pass
    
    @abstractmethod
    def print_all(self):
        pass
    
    def get_type(self) -> Type:
        return self._type

    def is_valued(self) -> int:
        return self._val