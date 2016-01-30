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

'''
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
        edges.append([ content[0], content[2] ])

    else:
        values = content[2].split(',')
        for i in range(len(values)):
            edges.append([ content[0], values[i] ])

cycle = eulerian(nodes, edges)

print cycle

f = open('resp.txt', 'w')
f.write(list(reversed(cycle))[0])
for elem in list(reversed(cycle))[1:]:
    f.write('->'+elem)
f.close()
'''
