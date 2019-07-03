from structs.graph import *
from structs.adj_list import AdjList
from structs.adj_mat import AdjMatrix
# import tkinter as tk
from tkinter.filedialog import askopenfilename
def read_file(fileName):
    '''Realiza a leitura do arquivo texto que contem 
    o grafo, recebe nome do arquivo'''
    f = open(fileName, "r")
    contents = f.read().split("\n")
    return contents
def open_file_():
    filename = askopenfilename()
    return filename

def generate_graph(contents: list, val: bool, t_struct: bool, is_graph: bool):
    """Função recebe uma lista de arestas e cria o grafo
        t_struct: True => AdjList e False => AdjMat
    """
    if is_graph==True:
        _type = Type.GRAPH
        # print('type: ',_type)
        # input()
    else:
        _type = Type.DIGRAPH
        # print('type: ',_type)
        # input()
    if len(contents[2].split()) == 3:
        val = True
    else:
        val = False
    
    if t_struct:
        graph = AdjList(int(contents[1]), _type, val)
    else:
        graph = AdjMatrix(int(contents[1]), _type, val)
    for x in contents[2:]:
        x = x.split()
        if(len(x) == 1):
            graph.make_relation(x[0])
        elif(len(x) == 2):
            graph.make_relation(x[0], x[1])
        else:
            graph.make_relation(x[0], x[1], int(x[2]))

    # graph.print_all()
    return graph