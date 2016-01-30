import random

def main(Dna,k,t):
    BestMotifs=[]
    Motifs = []
    for string in Dna:
        motif = random.choice( [ string[i:i+k] for i in range(len(string)-k+1) ] )
        Motifs.append(motif)

    BestMotifs = Motifs[:]

    while 1==1:
        prof = Profile(Motifs)
        Motifs = genMotifs(prof, Dna)

        if score(Motifs) < score(BestMotifs):
            BestMotifs=Motifs
        else:
            return BestMotifs

def sim(Dna, k, t):
    m = main(Dna,k,t)
    for i in range(10):
        n = main(Dna,k,t)
        if score(n) < score(m):
            m = n

    print "\n".join(m)

def genMotifs(prof, Dna):
    Motifs = []
    for string in Dna:
        k = len(prof)
        motif = most_prob( string, k, prof)
        Motifs.append(motif)
    return Motifs

def Profile(Motifs):
    prof=[]
    for i in range(len(Motifs[0])):
        A=C=G=T=1.0
        for j in range(len(Motifs)):
            if Motifs[j][i]=='A':
                A+=1
            if Motifs[j][i]=='C':
                C+=1
            if Motifs[j][i]=='G':
                G+=1
            if Motifs[j][i]=='T':
                T+=1
        n=A+C+G+T
        prof.append([A/n,C/n,G/n,T/n])
    return prof

def most_prob(text,k,prof):
    kmers = [ text[i:i+k] for i in range(len(text)-k+1) ]
    bestk= kmers[0]
    for kmer in kmers:
        if probability(kmer,prof)>probability(bestk,prof):
            bestk=kmer
    return bestk


def probability(kmer,profile):
    p=1
    for i in range(len(profile)):
        p_A=profile[i][0]
        p_C=profile[i][1]
        p_G=profile[i][2]
        p_T=profile[i][3]
        if kmer[i]=='A':
            p*=p_A    
        if kmer[i]=='C':
            p*=p_C 
        if kmer[i]=='G':
            p*=p_G 
        if kmer[i]=='T':
            p*=p_T
    return p

def score(motifs):
    s=0
    for i in range(len(motifs[0])):
        lst=[]
        for k in range(len(motifs)):
            lst.append(motifs[k][i])
        for j in range(len(motifs)):
           if motifs[j][i] != max(set(lst), key=lst.count):
               s+=1
    return s


f=open('data.txt')
    
file=[]
for line in f:
    file.append(line[:-1])
f.close()
k,t=int(file[0].split(" ")[0]),int(file[0].split(" ")[1])
Dna=[]
for i in range(1,len(file)):
    Dna.append(file[i])


sim(Dna,k,t)
