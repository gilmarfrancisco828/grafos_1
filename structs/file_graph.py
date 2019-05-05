#coding utf-8

class File():
    _arquivo = None
    _text = []
    
    @staticmethod
    def read_file(filename):
        File._arquivo = open(filename,'r')
        for x in File._arquivo:
            File._text.append(x)
    
    @staticmethod
    def close_file():
        if not File._arquivo == None:
            File._arquivo.close()

    @staticmethod
    def get_vertexes_qtd():
        #print(File._text[0])
        return int(File._text[0])
    
    @staticmethod
    def is_digraph():
        return  bool(File._text[0])

    @staticmethod
    def is_graph():
        return not is_digraph()

    @staticmethod
    def get_vertexes():
        i = 2
        vert_list = []
        while i < len(File._text):
            for x in File._text[i]:
                if x.isnumeric() and x not in vert_list:
                    vert_list.append(x)
            i += 1
        return vert_list
    
    @staticmethod
    def get_edges():
        i = 2
        edges = []
        while i < len(File._text):
            edges.append(File._text[i])
            i += 1
        return edges
