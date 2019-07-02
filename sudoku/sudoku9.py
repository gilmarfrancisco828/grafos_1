import matplotlib.pyplot as plt
import networkx as nx
import sys
import math
size = 9
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

def welshpowell(g):
    for node in g.node:
        if not g.node[node]['status']:
            for e in g.neighbors(node):
                if g.node[e]['status']:
                    try:
                        g.node[node]['color'].remove(g.node[e]['color'])
                    except:
                        pass
   

def update(g):
    for node in g.node:
        if not g.node[node]['status'] and len(g.node[node]['color']) == 1:
            g.node[node]['status'] = True
            g.node[node]['color'] = g.node[node]['color'][0]


def clear(g):
    for node in g.node:
        if g.node[node]['status'] and type(g.node[node]['color']) != int:
            g.node[node]['status'] = False


def leleo(g):
    for i in range(size):
        for j in range(size):
            if not g.node[nodes[i][j]]['status']:
                g.node[nodes[i][j]]['status'] = True
                welshpowell(g)
                update(g)
    clear(g)

def main(argv):
    # filename = argv[1]
    filename = 'sudoku/text1.txt'
    
    # create graph
    g = nx.Graph()

    # open and read file
    fp = open(filename, 'r')
    data = fp.read().split('\n')
    data.remove('')
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
            for k in range(i,size-1):
                g.add_edge(nodes[i][j], nodes[k+1][j])
    
    for i in range(size):
        for j in range(size-1):
            for k in range(j,size-1):
                g.add_edge(square[i][j], square[i][k+1])

    for i in range(size):
        leleo(g)
        welshpowell(g)
        update(g)
    
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
    nx.draw_networkx(g, pos=pos, with_labels=True)
    axs.set_axis_off()
    # axs[0].axis('tight')
    # axs[0].axis('off')
    # axs[0].table(cellText=original,loc='center')
    # # axs[0].table.
    # axs[1].axis('tight')
    # axs[1].axis('off')
    # axs[1].table(cellText=result, loc='center')
    plt.show()
    

if __name__ == '__main__':
    main(sys.argv)
