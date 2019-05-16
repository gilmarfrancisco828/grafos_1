#coding utf-8

from structs.graph import Type
from structs.adj_list import *
from structs.adj_mat import *
from algorithms.BFS import *
from algorithms.DFS import *
from algorithms.DIJKSTRA import *
from algorithms.KRUSKAL import *
from algorithms.PRIM import *
from algorithms.BELLMAN_FORD import *
from algorithms.KRUSKAL import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from structs.file_graph import File
from app.print_path_BFS import *
from app.print_times import *
from app.is_connected import *
from app.minimum_path import *

class Controller(object):
    "A classe controller, seguindo o padrão MVC, será a responsável por fazer o interfaceamento entre \no usuário (cliente main) e a implementação das estruturas e respectivos métodos."
    def __init__(self):
        self._G = None
        self._contents = []
    
    def DFS(self, s):
        "método para realizar o algoritmo de Depth-First Search"
        DFS_res = DFS(self._G, s, True)
        print_times(DFS_res)
        input()
    
    def BFS(self, s):
        "método para realizar ao algoritmo Breadth-First Search"
        BFS_res = BFS(self._G, s)
        print_path(BFS_res, s)
        input()
    
    def prim(self, s):
        "método que utiliza o algoritmo de prim para encontrar uma árvore geradora mínima"
        if self._G.is_valued():
            prim_res = prim(self._G, s)
            print(prim_res)
            input()
        
    def kruskal(self):
        if self._G.is_valued():
            kruskal_res = KRUSKAL(self._G)
            print('Arestas: ',*kruskal_res)
            input()    
    
    def dijkstra(self, s):
        "método que utiliza o algoritmo de Dijkstra para encontrar o caminho mínimo\n de um vértice para todos os outros"
        self._G.set_num_edges(self.get_edges())            
        dijkstra_res = DIJKSTRA(self._G, s)
        dijkstra_res.print_dijkstra(s)
        input()
        
    def bellman_ford(self, s):
        "método que utiliza o algoritmo de Bellman-Ford para encontrar o caminho mínimo\n de um vértice para todos os outros"
        bellman_ford_res = bellman_ford(self._G, s)
        bellman_ford_res.print_bellman_ford(s)
        input()
    
    def caminho_entre_vertex(self, s, t):
        "método para verificar se existe caminho entre dois vértices"
        print('1 - Caminho usando BFS')
        print('2 - Caminho usando DFS')
        op = input()
        if op == '1':
            res = BFS(self._G, s)
            print_path(res, t)
            input()
        else:
            res = DFS(self._G, s)
            print_path(res, t)
            input()

    def is_conected(self):
        "método para verificar se um grafo é conexo"
        is_connected(self._G)
        input()
        
    
    def is_graph(self):
        return False if self._contents[0] == 0 else True
        pass

    def get_contents(self):
        'Retorna a lista com os elementos do arquivo de grafos'
        return self._contents

    def create_graph(self, contents: list, t_struct: bool, tipo, is_valued:bool):
        """Função recebe uma lista de arestas e cria o grafo
            t_struct: True => AdjList e False => AdjMat
        """
        if t_struct:
            self._G = AdjList(int(self._contents[1]), Type.DIGRAPH, is_valued)
        else:
            self._G = AdjMatrix(int(self._contents[1]), Type.DIGRAPH, is_valued)
        for x in contents[2:]:
            x = x.split()
            # print(x)
            # input('check x')
            if(x == []):
                return
            if(len(x) == 1):
                self._G.make_relation(x[0])
            elif(len(x) == 2):
                self._G.make_relation(x[0], x[1])
            else:
                self._G.make_relation(x[0], x[1], int(x[2]))
          
    def show_folders(self):
        "método para procurar o arquivo que contém o grafo ou dígrafo"
        Tk().withdraw()
        filename = askopenfilename()
        self._arq = File()
        self._contents = File.read_file(filename)
   
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
        edges = len(self._contents)-2
        return edges
        
    def select_vertex(self,show=True):
        if show == True:
            self._G.print_all_vertexes()
        s = input('Insira o vértice: ')
        return s