def degree(node,edges):
    in_ = out = 0
    for edge in edges:
        if node == edge[0]:
            out += 1
        if node == edge[1]:
            in_ += 1
    return out-in_

def pathToCycle(nodes, edges):
    unbnodes = []

    for node in nodes:
        if degree(node, edges) < 0 :
            unbnodes.append(node)
            lastNode = node
        if degree(node, edges) > 0:
            unbnodes.append(node)
            firstNode = node

    edges.append([lastNode,firstNode])
    return [lastNode, firstNode]

def hasunmarkededges(u, markedEdges, edges):
    for edge in edges:
        if u == edge[0] and edge not in markedEdges:
            return edge[1], True
    return u, False
    
def eulerian(nodes, edges):
    stack = [nodes[0]]
    markedEdges = []
    cycle = []

    while stack != []:
        u = stack[-1]
        w, condition =  hasunmarkededges(u, markedEdges, edges)
        if condition:
            stack.append(w)
            markedEdges.append([u,w])
        else:
            stack.pop()
            cycle.append(u)
    return cycle

#obtencao do grafo
f = open('data.txt')
lines = [ elem[:-1] for elem in f.readlines() ]
f.close()

nodes = []
edges = []
for line in lines:
    content = line.split(' ')
    nodes.append(content[0])
    if len(content[2]) == 1:
        nodes.append(content[2])
        edges.append([ content[0], content[2] ])
    else:
        values = content[2].split(',')
        for i in range(len(values)):
            nodes.append(values[i])
            edges.append([content[0],values[i]])

nodes = list(set(nodes))

extraEdge = pathToCycle(nodes,edges)

cycle = eulerian(nodes, edges)

path = [ cycle[:-1][-i] for i in range (1, len(cycle)) ]

for i in range(len(path)-1):
    if [path[i] , path[i+1]] == extraEdge:
        start = i+1

path = path[start:] + path[:start]


f = open('resp.txt', 'w')
f.write(path[0])
for elem in path[1:]:
    f.write('->'+elem)
f.close()

