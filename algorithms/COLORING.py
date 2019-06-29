from structs.graph import Graph
from algorithms.DFS import *
from algorithms.TRANSPOSE import *
from algorithms.PRINT_GRAPH import *
from algorithms.MINIMUM_PATH_AOG import *
import random

class ColoringAux():

    def __init__(self, G):
        self.colors = {}
        self.cc     = 0

def bigger_degree(G: Graph):
    aux = []
    cont = 0
    for i in G.vertexes:
        print('Valor de i: ',i)
        if(len(i) < len(aux)):
            aux = i
            cont +=1
        aux = i
        print("len(aux): \n  valor de aux: ",len(aux), aux)
    print('contador: ',cont)
    return cont


def paint(Vk, aux, G):
    flag = False
    if Vk in aux.colors.keys():
        return
    if len(aux.colors) == 0:
        aux.colors[Vk] = aux.cc
        aux.cc += 1
    else:
        for v in aux.colors:
            if G.is_adjacent(Vk, v):
                continue
            else:
                aux.colors[Vk] = aux.colors[v]
                flag = True
    if flag == False:
        aux.cc += 1
        aux.colors[Vk] = aux.cc
            

def coloring(G: Graph):
    if G.get_len() == 0:
        return None
    aux = ColoringAux(G)
    u = bigger_degree(G)
    coloring_vertex(G, u, aux)
    return aux

def coloring_vertex(G: Graph, Vk, aux):
    paint(Vk, aux, G)
    for Vj in G.vertexes[Vk]:
        coloring_vertex(G, Vj, aux)