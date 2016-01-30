'''CODE CHALLENGE: Implement MEDIANSTRING.
     Input: An integer k, followed by a collection of strings Dna.
     Output: A k-mer Pattern that minimizes d(Pattern, Dna) among
all k-mers Pattern. (Return any one if there are multiple medium strings.)'''
import itertools

def main(Dna, k):
    BestPattern='A'*k
    for Pattern in possibilities(k):
        d_Pat_Dna=d_Best_Dna=0
        for i in range(len(Dna)-1):
            d_Pat_Dna+=d(Pattern,Dna[i])
            d_Best_Dna+=d(BestPattern,Dna[i])
        if d_Pat_Dna < d_Best_Dna:
            BestPattern=Pattern
    print(BestPattern)


def possibilities(k):
    p=list(itertools.product('ACTG', repeat=k))
    pn=[]
    for elem in p:
        i="".join(str(elem).split("', '"))
        a=i[2:-2]
        pn.append(a)
    return pn

def d(pattern,text):
    minSample=text[:len(pattern)]
    for i in range(len(text)-len(pattern)):
        sample=text[i:i+len(pattern)]
	if dist(pattern,sample)<dist(pattern,minSample):
            minSample=sample
    return dist(pattern,minSample)

def dist(s1,s2):
    score=0
    for i in range(len(s1)):
	if s1[i]!=s2[i]:
	    score+=1
    return score



arq=raw_input("Digite o nome do arq: ")
if arq=='n':
    k=int(raw_input("Escreva k: "))
    Dna=[]
    get=input("escreva Dna:")
    while get!='':
        Dna.append(get)
        get=input()
else:
    file=open(arq)
    content=file.read()
    k=int(content[0])
    gDna=content[1:]
    Dna=gDna.split('\n')[1:]
main(Dna,k)
