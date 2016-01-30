from genomepath import spell

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

def kmerbruijn(name):
    data = open(name)
    content = data.read()
    data.close()

    k = int(content[0])
    d = int(content[2])
    pairs = [ [elem[:k], elem[-k:]] for elem in [elem for elem in content.split()][2:] ]

    nodes = []
    for pair in pairs:
        nodes.append([ pair[0][:k], pair[1][:k] ])
        nodes.append([ pair[0][-k:], pair[1][-k:] ])

    nodes = sorted(list(set(nodes)))

    return nodes, pairs

def eulerianpath(nodes,pairs):
    extraEdge = pathToCycle(nodes,edges)

    cycle = eulerian(nodes, edges)

    path = [ cycle[:-1][-i] for i in range (1, len(cycle)) ]

    for i in range(len(path)-1):
        if [path[i] , path[i+1]] == extraEdge:
            start = i+1

    return path[start:] + path[:start]


def main():
    nodes, pairs = kmerbruijn('data.txt')
    print 'nodes: ', nodes
    print 'pairs: ', pairs
#    cycle = eulerian(nodes,edges)
#    print cycle[:-1]

main()
