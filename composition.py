def Composition(k, Text):
    arq = open("resp.txt", 'w')
    comp = []
    for i in range(len(Text)-k+1):
        comp.append(Text[i:i+k])
    comps = comp.sort()
    arq.write('\n'.join(comp))

a = open("data.txt")
texto = a.read()
lista = texto.split('\n')
k = int(lista[0])
t = lista[1]
Composition(k,t)
