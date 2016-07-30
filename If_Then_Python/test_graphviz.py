from graphviz import Digraph
import re

file_ = open('Human_Resource_Text.txt','r')
line = file_.readlines()
node_pos1 = []
node_pos2 = []
nodes = []
temp = "Start"
node_pos1.append(temp)
nodes_type = {}
nodes_type[temp] = 'rect'
for item in line:
    print item
    if 'if ' not in item.split('\n')[0]:
        node_pos1.append(item.split('\n')[0])
        a = (temp, item.split('\n')[0])
        temp = item.split('\n')[0]
        nodes_type[temp] = 'rect'
        nodes.append(a)
    else:
        if_clause = item.split(',')
        for elements in if_clause:
            pattern1 = re.findall('(?<=[Ii]f ).*?(?= else)', elements,re.U)
            node_pos1.append(pattern1[0])
            a = (temp,pattern1[0])
            nodes_type[pattern1[0]] = 'diamond'
            nodes.append(a)
            pattern2 = re.findall('(?<=else ).*', elements,re.U)
            node_pos2.append(pattern2[0])
            a = (pattern1[0],pattern2[0])

            nodes_type[pattern2[0]] = 'rect'

            nodes.append(a)
            temp = pattern1[0]



# here is the node counter 
n_c = 0
label_dict = {}
dot = Digraph(comment='Human Resource')
for key in nodes_type:
    dot.node(str(n_c),key,shape = nodes_type[key])
    label_dict[key] = str(n_c)
    n_c += 1
count = 0
for element in nodes:
    if count == 2:
        dot.edge(label_dict[element[0]], label_dict[element[1]], label = 'Yes',constraint='true')
        count = 0
    elif count ==1:
        dot.edge(label_dict[element[0]], label_dict[element[1]],label = 'No', constraint='true')
        count += 1
    else:
        dot.edge(label_dict[element[0]], label_dict[element[1]], constraint='true')
    if nodes_type[element[1]] == 'diamond':
        count += 1
dot.render('test-output/HR_Graph.gv',view=True)
# if edge labels is not specified, numeric labels (0, 1, 2...) will be used
#draw_graph(graph)
