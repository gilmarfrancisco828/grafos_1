

class File(object):
    self._arquivo = None
    self._text = []

    def __init__(self, file_name):
        self._arquivo = open(file_name, 'r')
        self._text = []

    def read_file():
        for x in _arquivo:
            self._text.append(x)

    def close_file(arq):
        if arq is not None:
            arq.close()

    def get_edges_qtd():
        return int(self._text[1])
    
    def is_digraph():
        return  int(self._text[0])

    def is_graph():
        return not is_digraph()

    def get_edges():
        pass