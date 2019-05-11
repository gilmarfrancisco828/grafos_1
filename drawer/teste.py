try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx

G=nx.DiGraph()

G.add_edge('a','b',weight=0.6)
G.add_edge('a','c',weight=0.2)
G.add_edge('c','d',weight=0.1)
G.add_edge('c','e',weight=0.7)
G.add_edge('c','f',weight=0.9)
G.add_edge('a','d',weight=0.3)

# elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
# esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

pos=nx.spring_layout(G) # positions for all nodes

# # nodes
nx.draw_networkx_nodes(G,pos,node_size=700)

# # edges
nx.draw_networkx_edges(G,pos,
                    width=6)
# nx.draw_networkx_edges(G,pos,edgelist=esmall,
#                     width=6,alpha=0.5,edge_color='b',style='dashed')

# # labels
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# nx.draw_random(G)

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display