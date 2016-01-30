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
    
    kmers = [ elem[:-1] for elem in data.readlines() ][1:]
    data.close()
    k = len(kmers[0])-1

    nodes = []
    
    for kmer in kmers:
        nodes.append( kmer[:k] )
        nodes.append( kmer[-k:] )

    nodes = sorted(list(set(nodes)))

    edges = []
    
    for node in nodes:
        adjacent = []
        for kmer in kmers:
            if kmer[:k] == node:
                adjacent.append( kmer[-k:] )
        for elem in adjacent:
            edges.append([node,elem])
    
    return nodes, edges

def eulerianpath(nodes,edges):
    extraEdge = pathToCycle(nodes,edges)

    cycle = eulerian(nodes, edges)

    path = [ cycle[:-1][-i] for i in range (1, len(cycle)) ]

    for i in range(len(path)-1):
        if [path[i] , path[i+1]] == extraEdge:
            start = i+1

    return path[start:] + path[:start]


def main():
    nodes, edges = kmerbruijn('data.txt')
    cycle = eulerian(nodes,edges)
    print cycle[:-1]
