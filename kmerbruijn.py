

data = open('data.txt')

kmers = [ elem[:-1] for elem in data.readlines() ]
data.close()
k = len(kmers[0]) - 1
nodes = []

for kmer in kmers:
    nodes.append( kmer[:k] )
    nodes.append( kmer[-k:] )

nodes = sorted(list(set(nodes)))

edges = []

for node in nodes:
    edge = [node]
    adjacent = []
    for kmer in kmers:
        if kmer[:k] == node:
            adjacent.append( kmer[-k:] )
    adjacentord = sorted(adjacent)
    edge.append(adjacentord)
    edges.append(edge)

resp = open('resp.txt', 'w')

for edge in edges:
    if len( edge[1] ) != 0 :
        resp.write( edge[0] + ' -> ' )
        for e in range( len(edge[1]) - 1 ):
            resp.write( edge[1][e] + ',')
        resp.write( edge[1][-1] + '\n')

resp.close()
