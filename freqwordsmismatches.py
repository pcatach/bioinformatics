import approximatepc, reverse, itertools

def fwp(text, k, d):
    prekmers = itertools.product('AGCT',repeat = k)
    kmers = [ ''.join(str(i) for i in elem) for elem in prekmers ]
    fw = []
    maxscore = 0
    mskmers = []
    for kmer in kmers:
        rkmer = reverse.FindReverse(kmer)
        score = approximatepc.apc(text, rkmer,d)
        score2 = approximatepc.apc(text, kmer,d)
        if score+score2 > maxscore:
            maxscore = score+score2
            mskmers = [rkmer, kmer]
        elif score == maxscore:
            mskmers.append(kmer)
            mskmers.append(rkmer)
    return mskmers
            

text = raw_input("Digite text: ")
k = int(raw_input("Digite k: "))
d = int(raw_input("Digite d: "))
lista = fwp(text, k, d)

for elem in lista:
    print ''.join( str(i) for i in elem ), ' ',
