import matplotlib.pyplot as plt
import networkx as nx
import sys
import math
def solve_sudoku(n, g, data):
    size = n
    root = int(math.sqrt(size))
    nodes = []
    for i in range(0, size):
        line = []
        for j in range(0, size):
            line.append("{}x{}".format(i, j))
        nodes.append(line)

    square = []
    for j in range(0, size):
        quadrado = []
        for i in range(0, size, root):
            quadrado.append(["{}x{}".format(j, x) for x in range(i, i+root)])
        square.append(quadrado)

    malha = []
    for i in range(0, size, root):
        for j in range(0, root):
            linha = []
            for k in range(i, i+root):
                # print("{}x{}".format(k, j), end=' ')
                linha = linha + square[k][j]
            # print()
            malha.append(linha)
        # print()
    square = malha
    sudoku = []
    for line in data:
        sudoku.append(line.split(' '))

    # create node with color and status
    original = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(sudoku[i][j])
            if sudoku[i][j] == 'x':
                g.add_node(nodes[i][j], color=[[i for i in range(1,size+1)]], status=False)
            else:
                # print(int(sudoku[i][j]))
                g.add_node(nodes[i][j], color=int(sudoku[i][j]), status=True)
        original.append(line)

    # create edges of rows
    for i in range(size):
        for j in range(size-1):
            for k in range(j,size-1):
                g.add_edge(nodes[i][j], nodes[i][k+1])
    
    # create edges of columns
    for i in range(size-1):
        for j in range(size):
            for k in range(i, size-1):
                g.add_edge(nodes[i][j], nodes[k+1][j])
    
    for i in range(size):
        for j in range(size-1):
            for k in range(j, size-1):
                g.add_edge(square[i][j], square[i][k+1])

    for i in range(size):
        leleo(g, nodes, size)
        welshpowell(g, nodes)
        update(g, nodes)
    
    result = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(g.node[nodes[i][j]]['color'])
            print(g.node[nodes[i][j]]['color'], end=' '),
        print()
        result.append(line)

    #nx.draw_networkx(g, pos=nx.spring_layout(g), with_labels=True)
    fig, axs =plt.subplots(nrows=1, ncols=1, figsize=(25,15))
    pos=nx.circular_layout(g)
    axs.set_axis_off()
    nx.draw_networkx(g, pos=pos, with_labels=True)
    plt.show()
    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(25,15))
    axs[0].axis('tight')
    axs[0].axis('off')
    axs[0].table(cellText=original,loc='center')
    # axs[0].table.
    axs[1].axis('tight')
    axs[1].axis('off')
    axs[1].table(cellText=result, loc='center')
    plt.show()

def welshpowell(g, node):
    for n in g.node:
        if not g.node[n]['status']:
            for e in g.neighbors(n):
                if g.node[e]['status']:
                    try:
                        g.node[n]['color'].remove(g.node[e]['color'])
                    except:
                        pass
   

def update(g, node):
    for n in g.node:
        if not g.node[n]['status'] and len(g.node[n]['color']) == 1:
            g.node[n]['status'] = True
            g.node[n]['color'] = g.node[n]['color'][0]


def clear(g, node):
    for n in g.node:
        if g.node[n]['status'] and type(g.node[n]['color']) != int:
            g.node[n]['status'] = False


def leleo(g, node, size):
    for i in range(size):
        for j in range(size):
            if not g.node[node[i][j]]['status']:
                g.node[node[i][j]]['status'] = True
                welshpowell(g, node)
                update(g, node)
    clear(g, node)

