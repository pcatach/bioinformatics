from itertools import product
import random

def generateKmers(k):
    return [ ''.join(x) for x in product('01', repeat=k) ]

def bruijn(kmers):
    k = len(kmers[0]) - 1

    nodes = []
    edges = []
    for kmer in kmers:
        edges.append( [ kmer[:k], kmer[-k:] ] )
        nodes.append( kmer[:k] )
        nodes.append( kmer[-k:] )

    nodes = list(set(nodes))
    
    return nodes, edges

def walk(node, edges):
    edgesCopy = edges[:]
    for edge in edges:
        if edge[0] == node:
            edges.remove(edge)
            return edge[1]

def randomCycle(node1, edges):
    inicial = node1
    node2 = walk(node1, edges)
    cycle = [[node1,node2]]
    while node2 != inicial:
        node1 = node2
        node2 = walk(node1, edges)
        cycle.append([node1, node2])
    return cycle

def selectStart(cycle, edges):
    for i in range(len(cycle)):
        for edge in edges:
            if cycle[i][0] == edge[0]:
                return i

def traverse(start, cycle):
    return cycle[start:] + cycle[:start]

def eulerian(nodes, edges):
    node1 = random.choice(nodes)
    cycle = randomCycle(node1, edges)
    while edges != []:
        newStartPos = selectStart(cycle, edges)
        newStart = cycle[newStartPos][0]
        cycle = traverse(newStartPos, cycle)
        cycle += randomCycle(newStart, edges)
    return cycle

k = int(raw_input('k = '))
kmers = generateKmers(k)
nodes, edges = bruijn(kmers)
cycle =  eulerian(nodes, edges)
for i in range(len(cycle)):
    if cycle[i][0] == 0*(k-1):
        break

cycle = cycle[i:] + cycle[:i]

string = ''
for edge in cycle:
    string += edge[0][0]
print string[::-1]
