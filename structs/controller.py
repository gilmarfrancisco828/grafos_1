#coding utf-8

from adj_list import AdjList
from graph import Type as tp
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from file_graph import File


class Controller(object):
    _adjg     = None
    _adjdg    = None
    _matrixg  = None
    _matrixdg = None

    def show_folders(self):
        Tk().withdraw()
        filename = askopenfilename()
        self._arq = File()
        File.read_file(filename)

    def close_file(self):
        File.close_file()

    def show_menu(self):
        print('S - Sair\n'
              '1 - Escolher representação computacional\n'
              '2 - Busca em Profundidade\n'
              '3 - Busca em largura\n'
              '4 - Caminho entre dois vértices\n'
              '5 - Verificar se um grafo é conexo\n'
              '6 - Árvore geradora mínima - Prim\n'
              '7 - Árvore geradora mínima - Kruskal\n'
              '8 - Caminho mínimo - Dijkstra\n'
              '9 - Caminho mínimo - Bellman-Ford\n')
        op = str(input('Digite o valor associado a opção escolhida: '))
        return op

    def get_vertexes(self):
        self._vertexes = File.get_vertexes()
        print(*l)

    def get_edges(self):
        self._edges = File.get_edges()
        
