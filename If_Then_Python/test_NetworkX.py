import networkx as nx
import matplotlib.pyplot as plt
import re
def draw_graph(graph, node_pos1,node_pos2, labels=None, graph_layout='spring',
               node_size=4400, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='red', edge_alpha=0.3, edge_tickness=3,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()
##    for i,item1 in enumerate(node_pos1):
##        G.add_node(item1,pos = "i,1")
##    for j,item2 in enumerate(node_pos2):
##        G.add_node(item2,pos = (j,0)
    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)
    pos = {}
    for i, item1 in enumerate(node_pos1):
        pos[item1] = (i,1)
    for j, item2 in enumerate(node_pos2):
        pos[item2] = (j+2,0)
    graph_pos = pos
    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
##    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
##                                 label_pos=edge_text_pos)

    # show graph
    plt.show()


file_ = open('Human_Resource_Text.txt','r')
line = file_.readlines()
node_pos1 = []
node_pos2 = []
nodes = []
temp = "Start"
node_pos1.append(temp)
for item in line:
    print item
    if 'if ' not in item.split('\n')[0]:
        node_pos1.append(item.split('\n')[0])
        a = (temp, item.split('\n')[0])
        temp = item.split('\n')[0]
        nodes.append(a)
    else:
        if_clause = item.split(',')
        for elements in if_clause:
            pattern1 = re.findall('(?<=[Ii]f ).*?(?= else)', elements,re.U)
            node_pos1.append(pattern1[0])
            a = (temp,pattern1[0])
            nodes.append(a)
            pattern2 = re.findall('(?<=else ).*', elements,re.U)
            node_pos2.append(pattern2[0])
            a = (pattern1[0],pattern2[0])
            nodes.append(a)
            temp = pattern1[0]
            
                
            
graph = nodes

# you may name your edge labels
labels = map(chr, range(65, 65+len(graph)))
draw_graph(graph,node_pos1,node_pos2,labels)

# if edge labels is not specified, numeric labels (0, 1, 2...) will be used
#draw_graph(graph)
