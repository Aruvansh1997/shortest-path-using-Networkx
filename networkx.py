#networkx for graph
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

source=6
target=7
g = nx.Graph() 
df=pd.read_csv(r'NodeList.csv')
df_edge=pd.read_csv(r'EdgeList.csv')
# weighted edge
edge = list(zip(df_edge.node1,df_edge.node2,df_edge.wt))
# node coordinates
xy=list(zip(df.x,df.y))
pos = dict(zip(df.node,xy))

# adding edges
g.add_weighted_edges_from(edge)
# to make the whole graph
nx.draw_networkx(g,pos=pos)
#dynamic addition of edges
pos[6]=(18.4, 19.9)
pos[7]=(20.2, 19.9)
g.add_edge(6, 1, weight=5)
g.add_edge(6, 5, weight=5)
g.add_edge(4, 7, weight=2)

length,path =nx.single_source_dijkstra(g,source=source,target=target)
path_edges =set(zip(path,path[1:]))
print(path,length)
#highlighting the path of min distance
nx.draw_networkx(g,pos,nodelist=path,node_color='r',edgelist=path_edges,edge_color='r',with_labels=True,)
g.remove_node(6)
g.remove_node(7)
plt.show()
