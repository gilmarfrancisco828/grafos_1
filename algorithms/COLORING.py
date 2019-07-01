from structs.graph import Graph
from algorithms.DFS import *
from algorithms.TRANSPOSE import *
from algorithms.PRINT_GRAPH import *
from algorithms.MINIMUM_PATH_AOG import *
import random
from itertools import chain 

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
        
def get_spaced_colors(n):
    max_value = 16581375 #255**3
    interval = int(max_value / n)
    colors = [hex(I)[2:].zfill(6) for I in range(0, max_value, interval)]
    return [(int(i[:2], 16), int(i[2:4], 16), int(i[4:], 16)) for i in colors]            

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
        # input(G.vertexes)
        for v in G.vertexes:
            if v not in aux.colored.keys():
                coloring_vertex(G, v, aux)
    hex_colors = {}

    # print(aux.colored.keys())
    # input()
    cor = get_spaced_colors(aux.cc+1) #cria as cores na quantidade cromática
    # input(len(cor))
    flipped = {} 
  
    for key, value in aux.colored.items(): 
        if value not in flipped: 
            flipped[value] = [key] 
        else: 
            flipped[value].append(key) 
    print(flipped)
    print(len(flipped))
    i=0
    print(cor)
    print(len(cor))
    
    # input()
    while i < len(flipped):
        for x in flipped[i]:
            hex_colors[x] = '#%02X%02X%02X' % cor[i]
        i+=1
    
    
    # hex_colors[i] = '#%02X%02X%02X' % (aux.colored[i]*89, aux.colored[i]*12, aux.colored[i]*100)
    # print(cor)
        
    colors = {
        'hex': hex_colors
    }
    # print(colors)
    # input()
    PRINT_GRAPH(G, colors=colors, colors_fun=get_colors_coloring) 
    plt.title('Valor cromático: {0}'.format(aux.cc+1))
    plt.show()
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
    
    