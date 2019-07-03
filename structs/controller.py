#coding utf-8
import matplotlib.pyplot as plt
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
# from tkinter.filedialog import askopenfilename
from structs.file_graph import File
from app.print_path_BFS import *
from app.print_times import *
from app.is_connected import *
from app.minimum_path import *
from test.helper_leitura import *
from algorithms.PRINT_GRAPH import *
from algorithms.MINIMUM_PATH_AOG import *
from structs.graph import Type
from algorithms.BFS import *
from algorithms.COLORING import *
from algorithms.STRONGLY_CONNECTED_COMPONENTS import *
from algorithms.CONNECTED_COMPONENTS import *
from algorithms.DFS import *
from algorithms.DIJKSTRA import *
from algorithms.KRUSKAL import *
from algorithms.TRANSPOSE import *
from sudoku.sudoku import *
class Controller(object):
    "A classe controller, seguindo o padrão MVC, será a responsável por fazer o interfaceamento entre \no usuário (cliente main) e a implementação das estruturas e respectivos métodos."
    def __init__(self):
        self._G = None
        self._contents = []

    def build_graph(self):
        self.show_folders()
        isgraph = None
        # input(self._contents)
        # print(self._contents[0])
        if self._contents[0] == '0':
            isgraph = True
            # print('entrou true')
        else:
            isgraph = False
            # print('entrou false')
        # input(self._contents)
        # print(self._contents[0])
        # input()
        # print(isgraph)
        # input()

        self._G = generate_graph(self._contents, True, False, isgraph)
        


    def ctrl_connected_components(self):
        graph = self._G
        if self._G.is_graphb():
            res = connected_components(graph) 
        else:
            print('A entrada deve ser um grafo.')
            input()
        
    def ctrl_coloring(self):
        graph = self._G
        if self._G.is_graphb():
            result = coloring(graph)
        else:
            print('A entrada deve ser um grafo.')
            input()

    def ctrl_mst(self):
        graph = self._G
        if self._G.is_graphb():
            result = KRUSKAL(graph)
            graph = self._G
            fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(25, 15))
            # print(result)
            soma = 0
            for val in result:
                soma+=val[2]
        
            PRINT_GRAPH(graph, axes, "AGM - Kruskal - Custo Total: {}".format(soma), colors=result, colors_fun=get_colors_tree)
            plt.show() # display
        else:
            print('A entrada deve ser um grafo.')
            input()
    
    def get_len_edges(self, contents):
        return len(contents)-2

    def ctrl_shortest_path(self, s):
        graph = self._G
        graph.set_num_edges(self.get_len_edges(self._contents))
        result = DIJKSTRA(graph, s)
        edges = []
        textstr = 'Distâncias Mínimas:'
        for v in graph.vertexes:
            if v != s:
                soma = 0
                path = result.get_path(v)
                for u, w in path:
                    soma += graph.get_value(u, w)
                textstr += "\n{}: {}".format(v, soma)
                edges += path
        # print(soma)

        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(25, 15))
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        axes.text(0.05, 0.95, textstr, transform=axes.transAxes, fontsize=14, verticalalignment='top', bbox=props)

        PRINT_GRAPH(graph, axes, "Caminho Mínimo - Dijkstra - Início({})".format(s), colors=edges, colors_fun=get_colors_dij)
        plt.show() # display

    def ctrl_connectivity(self):
        print(self._G.is_graphb())
        if not self._G.is_graphb():
            colors, elements = STRONGLY_CONNECTED_COMPONENTS(self._G) 
        else:
            print('A entrada deve ser um dígrafo.')
            input()
    
    def ctrl_transpose(self):
        grapht = transpose(self._G)
        if not self._G.is_graphb():
            fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25,15))
            ax = axes.flatten()
            graph = self._G
            # print(graph.is_valued())
            PRINT_GRAPH(graph, ax[0], 'Original')
            grapht = transpose(graph)
            PRINT_GRAPH(grapht, ax[1], 'Transposto')
            # print(graph.vertexes['b'])
            plt.show() # display
        else:
            print('A entrada deve ser um dígrafo.')
            input()

    def ctrl_topological_sort(self):
        graph = self._G
        if not self._G.is_graphb():
            fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 15))
            PRINT_GRAPH(graph, axes[0], "Grafo", colors=None, colors_fun=get_colors_tree)
            
            order = TOPOLOGICAL_SORT(graph)
            edges= []
            order.reverse()
            # print(order)
            graph_caminho = AdjMatrix(graph.get_len(), Type.DIGRAPH, False)
            ant = order.pop(0)
            for v in order:
                edges.append((ant, v))
                graph_caminho.make_relation(ant, v)
                ant = v

            PRINT_GRAPH(graph_caminho, axes[1], "Ordem Topológica", colors=edges, colors_fun=get_colors_bfs)
            plt.show() # display
        else:
            print('A entrada deve ser um dígrafo.')
            input()

    def DFS(self, s):
        "método para realizar o algoritmo de Depth-First Search"
        DFS_res = DFS(self._G, s, True)
        print_times(DFS_res)
        input()
    
    def ctrl_BFS(self, s):
        graph = self._G
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 15))
        PRINT_GRAPH(graph, axes[0], "Grafo", colors=None, colors_fun=get_colors_tree)
            
        result = BFS(graph, s)
        edges= []
        order = list(result.q_path.queue)
        # print(order)
        # input(graph.get_type())
        if(graph.get_type() == Type.DIGRAPH):
            graph_caminho = AdjMatrix(graph.get_len(), Type.DIGRAPH, False)
        else:
            graph_caminho = AdjMatrix(graph.get_len(), Type.GRAPH, False)
        ant = order.pop(0)
        for v in order:
            edges.append((ant, v))
            graph_caminho.make_relation(ant, v)
            ant = v

        PRINT_GRAPH(graph_caminho, axes[1], "BFS", colors=edges, colors_fun=get_colors_bfs)
        plt.show() # display
    

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
        # if t_struct:
        self._G = AdjList(int(self._contents[1]), Type.DIGRAPH, is_valued)
        # else:
        #     self._G = AdjMatrix(int(self._contents[1]), Type.DIGRAPH, is_valued)
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
        filename = open_file_()
        # self._arq = File()
        self._contents = read_file(filename)
   
    def close_file(self):
        "método para fechar o arquivo do grafo atual"
        File.close_file()

    def show_menu(self):
        "método para ter acesso as opções que o programa oferece"
        print('S - Sair\n'
              '1 - Componentes Conexas\n'
              '2 - Coloração\n'
              '3 - Árvore Geradora Mínima\n'
              '4 - Caminho Mínimo\n'
              '5 - Conectividade\n'
              '6 - Transposição\n'
              '7 - Ordenação Topológica\n'
              '8 - Busca em Largura\n'
              '9 - Carregar um novo grafo\n'
              '10- Sudoku\n')
        op = str(input('Digite o valor associado a opção escolhida: '))
        return op

    def select_data_structure(self):
        "metodo para escolher a representação computacional que será usada para o grafo"
        print('1 - Lista de Adjacência\n'
              '2 - Matriz de Adjacência\n')
        a = int(input('Digite o número referente a escolha: '))
        return True if a == 1 else False

    def get_vertexes(self):
        vertices = "[ "
        for v in self._G.vertexes:
            vertices+="{} ".format(v)
        vertices+="]"
        return vertices
        
    def get_edges(self):
        edges = len(self._contents)-2
        return edges
        
    def select_vertex(self,show=True):
        if show == True:
            self._G.print_all_vertexes()
        s = input('Insira o vértice: ')
        return s
    
    def sudoku(ar):
        n = int(input('Entre com o tamanho do sudoku: '))
        # create graph
        g = nx.Graph()

        # open and read file
        # Tk().withdraw()
        # filename = askopenfilename()
        filename = askopenfilename()
        # filename = '/home/parafuso828/Documents/UNESP/3_SEM_1/Teoria de Grafos/TP01/grafos_1/sudoku/text1.txt'
        fp = open(filename, 'r')
        data = fp.read().split('\n')
        data.remove('')
        solve_sudoku(n, g, data)
        input()