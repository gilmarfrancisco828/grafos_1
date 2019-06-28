from enum import Enum
from abc import abstractmethod
from collections import defaultdict
from collections import OrderedDict
import collections

class OrderedDefaultdict(OrderedDict):
    """ A defaultdict with OrderedDict as its base class. """

    def __init__(self, default_factory=None, *args, **kwargs):
        if not (default_factory is None
                or isinstance(default_factory, collections.Callable)):
            raise TypeError('first argument must be callable or None')
        super(OrderedDefaultdict, self).__init__(*args, **kwargs)
        self.default_factory = default_factory  # called by __missing__()

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key,)
        self[key] = value = self.default_factory()
        return value

class Type(Enum):
    GRAPH = False
    DIGRAPH = True


class Graph(object):

    def __init__(self, _len: int, _type: Type, _val: bool):
        self._len = _len
        self._type = _type
        self._val = _val
        # self.vertexes = OrderedDefaultdict(dict)
        self.vertexes = defaultdict(dict)
        self._len_edges = None

    @abstractmethod
    def make_relation(self, a, b, val: int) -> bool:
        pass

    @abstractmethod
    def is_adjacent(self, a, b) -> bool:
        pass

    @abstractmethod
    def print_all(self):
        pass
    @abstractmethod
    def print_all_vertexes():
        pass

    def get_type(self) -> Type:
        return self._type

    def is_valued(self) -> bool:
        return self._val

    def get_len(self) -> int:
        return self._len

    def get_len_edges(self) -> int:
        return self._len_edges

    def set_num_edges(self, num_edges: int = None):
        self._len_edges = num_edges
