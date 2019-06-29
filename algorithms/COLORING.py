from structs.graph import Graph
from algorithms.DFS import *
from algorithms.TRANSPOSE import *
from algorithms.PRINT_GRAPH import *
from algorithms.MINIMUM_PATH_AOG import *
import random

class ColoringAux():

    def __init__(self, G):
        self.colored = {}
        self.cc     = 0
        

def bigger_degree(G: Graph):
    aux = 0
    v = None
    for i in G.vertexes:
        for j in G.vertexes[i]:
            if aux < len(G.vertexes[i]):
                aux = len(G.vertexes[i])
                v = i
    # input(v)
    return v

def paint(Vk, aux, G):
    flag = False
    if Vk in aux.colored.keys():
        return
    if len(aux.colored) == 0:
        aux.colored[Vk] = aux.cc
        # print('if[1] {0} received color: {1}'.format(Vk, aux.colored[Vk]))
        # aux.cc += 1
        return
    else:
        aux1 = aux.colored.copy()
        for v in aux1:
            if G.is_adjacent(Vk, v):
                continue
            else:
                flag = True
                aux.colored[Vk] = aux.colored[v]
                for adj in G.vertexes[Vk]:
                    if adj in aux.colored.keys():
                        if aux.colored[Vk] == aux.colored[adj]:
                            flag = False
                # print('else[1,2]{0} received color: {1}'.format(Vk, aux.colored[Vk]))
                if(flag == True):
                    return

    if flag == False:
        aux.cc += 1
        aux.colored[Vk] = aux.cc
        # print('if[2]{0} received color: {1}'.format(Vk, aux.colored[Vk]))
        
            

def coloring(G: Graph):
    if G.get_len() == 0:
        return None
    aux = ColoringAux(G)
    
    if G.get_len() == 1:
        for i in G.vertexes:
            aux.colored[i] = aux.cc
    else:    
        aux = ColoringAux(G)
        u = bigger_degree(G)
        coloring_vertex(G, u, aux)
    return aux

def coloring_vertex(G: Graph, Vk, aux):
    # print('vértice a ser colorido: ',Vk)
    # input()
    if Vk in aux.colored:
        return
    paint(Vk, aux, G)
    for Vj in G.vertexes[Vk]:
        # input(Vj)
        coloring_vertex(G, Vj, aux)