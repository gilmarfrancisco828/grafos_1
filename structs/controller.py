#coding utf-8

from graph import Type as tp
from adj_list import AdjList
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from file_graph import File


class Controller(object):
    "A classe controller, seguindo o padrão MVC, será a responsável por fazer o interfaceamento entre \no usuário (cliente main) e a implementação das estruturas e respectivos métodos."
    _adjg     = None
    _adjdg    = None
    _matrixg  = None
    _matrixdg = None

    def show_folders(self):
        "método para procurar o arquivo que contém o grafo ou dígrafo"
        Tk().withdraw()
        filename = askopenfilename()
        self._arq = File()
        File.read_file(filename)
   

    def close_file(self):
        "método para fechar o arquivo do grafo atual"
        File.close_file()

    def show_menu(self):
        "método para ter acesso as opções que o programa oferece"
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

    def select_data_structure(self):
        "metodo para escolher a representação computacional que será usada para o grafo"
        print('1 - Lista de Adjacência\n'
              '2 - Matriz de Adjacência\n')
        return str(input('Digite o número referente a escolha: '))

    def get_vertexes(self):
        self._vertexes = File.get_vertexes()
        

    def get_edges(self):
        self._edges = File.get_edges()
        
    
    def DFS(self):
        "método para realizar o algoritmo de Depth-First Search"
        pass
    
    def BFS(self):
        "método referente ao algoritmo Breadth-First Search"
        pass
    
    def caminho_entre_vertex(self):
        "método para verificar se existe caminho entre dois vértices"
        pass

    def is_conected(self):
        "método para verificar se um grafo é conexo"
        pass
    
    def prim(self, s):
        "método que utiliza o algoritmo de prim para encontrar uma árvore geradora mínima"
        pass
    
    def dijkstra(self, s):
        "método que utiliza o algoritmo de Dijkstra para encontrar o caminho mínimo\n de um vértice para todos os outros"
        pass
    
    def bellman_ford(self):
        "método que utiliza o algoritmo de Bellman-Ford para encontrar o caminho mínimo\n de um vértice para todos os outros"
        pass