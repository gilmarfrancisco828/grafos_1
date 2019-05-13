#coding utf-8

from graph import Type
from AdjList import *
from AdjMatrix import *
from algorithms import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from file_graph import File


class Controller(object):
    "A classe controller, seguindo o padrão MVC, será a responsável por fazer o interfaceamento entre \no usuário (cliente main) e a implementação das estruturas e respectivos métodos."
    def __init__():
        self._G = None


    def create_graph(self, _len: int, _type: Type, _val: bool, _type_structure=None):
        if _type_structure == None:
            return False
        elif _type_structure == True:
            self._G = AdjList(_len, _type, _val)
        else:
            self._G = AdjMatrix(_len, _type, _val)
            

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
        a = int(input('Digite o número referente a escolha: '))
        return True if a == 1 else False


    def get_vertexes(self):
        self._vertexes = File.get_vertexes()
        

    def get_edges(self):
        self._edges = File.get_edges()
        
    
    def DFS(self):
        "método para realizar o algoritmo de Depth-First Search"
        self._G.DFS()
        #TODO: Print result
        
    
    def BFS(self):
        "método referente ao algoritmo Breadth-First Search"
        self._G.BFS
        
    
    def caminho_entre_vertex(self):
        "método para verificar se existe caminho entre dois vértices"
        pass

    def is_conected(self):
        "método para verificar se um grafo é conexo"
        pass
    
    def prim(self, s):
        "método que utiliza o algoritmo de prim para encontrar uma árvore geradora mínima"
        prim_res = self._G.prim(s)
        #TODO: Print result
        
    
    def dijkstra(self, s):
        "método que utiliza o algoritmo de Dijkstra para encontrar o caminho mínimo\n de um vértice para todos os outros"
        dikstra_aux = self._G.dijkstra(s)
        #TODO: Print result
        
    def kruskal(self, s):
        kruskal_res = self._G.kruskal(s)
        #TODO: Print result

    def bellman_ford(self):
        "método que utiliza o algoritmo de Bellman-Ford para encontrar o caminho mínimo\n de um vértice para todos os outros"
        bellman_ford_aux = self._G.bellman_ford(s)
        #TODO: Print result
    