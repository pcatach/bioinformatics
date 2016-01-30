def debruijn(text,k):
    edges, nodes = pathGraph(text, k)
    nodes = sorted(list(set(nodes)))

    f= open('resp.txt','w')

    alist = []

    for node in nodes:
        elem = [node]
        for edge in edges:
            if edge[:k-1] == node:
                elem.append( edge[-k+1:] )
        alist.append( elem )

    for elem in alist:
        if elem[0] != elem[1] and elem[0] != text[:-k+1]
        f.write( elem[0] + " -> " )
        for e in range(1,len(elem)-1):
            f.write( elem[e] + "," )
        f.write( elem[-1] + "\n" )

    f.close()

def pathGraph(text, k):
    edges = []
    nodes = []

    for i in range(len(text) - k + 1):
        edges.append( text[i:i+k] )

    for i in range(len(text) - k + 2):
        nodes.append( text[i:i+k-1] )

    return edges, nodes

k = input("Digite k: ")
text = raw_input("digite text: ")
debruijn(text,k)
