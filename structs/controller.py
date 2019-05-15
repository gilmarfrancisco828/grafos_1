#coding utf-8

from structs.graph import Type
from structs.adj_list import *
from structs.adj_mat import *
from algorithms import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from structs.file_graph import File


class Controller(object):
    "A classe controller, seguindo o padrão MVC, será a responsável por fazer o interfaceamento entre \no usuário (cliente main) e a implementação das estruturas e respectivos métodos."
    def __init__(self):
        self._G = None
        self._contents = []


    def read_file(fileName):
        '''Realiza a leitura do arquivo texto que contem 
        o grafo, recebe nome do arquivo'''
        f = open(fileName, "r")
        contents = f.read().split("\n")
        return contents

    def get_contents(self):
        'Retorna a lista com os elementos do arquivo de grafos'
        return self._contents

    def create_graph(self , contents: list, val: bool, t_struct: bool):
        """Função recebe uma lista de arestas e cria o grafo
            t_struct: True => AdjList e False => AdjMat
        """
        if t_struct:
            self._G = AdjList(int(contents[1]), Type.DIGRAPH, val)
        else:
            self._G = AdjMatrix(int(contents[1]), Type.DIGRAPH, val)
        for x in contents[2:]:
            x = x.split()
            if(len(x) == 1):
                self._G.make_relation(x[0])
            elif(len(x) == 2):
                self._G.make_relation(x[0], x[1])
            else:
                self._G.make_relation(x[0], x[1], int(x[2]))

        # graph.print_all()
          

    def show_folders(self):
        "método para procurar o arquivo que contém o grafo ou dígrafo"
        Tk().withdraw()
        filename = askopenfilename()
        self._arq = File()
        contents = File.read_file(filename)
   

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
        DFS_res = self._G.DFS()
        #TODO: Print result
        
    
    def BFS(self):
        "método referente ao algoritmo Breadth-First Search"
        BFS_res = self._G.BFS()
        
    
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

    def bellman_ford(self, s):
        "método que utiliza o algoritmo de Bellman-Ford para encontrar o caminho mínimo\n de um vértice para todos os outros"
        bellman_ford_aux = self._G.bellman_ford(s)
        #TODO: Print result
    