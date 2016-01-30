

def main(text,k,prof):
    kmers=getkmers(text,k)
    bestk='A'*k
    for kmer in kmers:
        if probability(kmer,prof)>probability(bestk,prof):
            bestk=kmer
    print(bestk)

def getkmers(text,k):
    l=[]
    for i in range(len(text)-k+1):
        l.append(text[i:i+k])
    return l


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

while 1==1:
    arq=input()
    f=open(arq)
    file=f.readlines()
    f.close()
    Text=file[0][:-1]
    k=int(file[1])
    Profile=[]
    for i in range(3,len(file)):
        position=[]
        for j in file[i].split(" "):
            position.append(float(j))
        Profile.append(position)
    
    main(Text,k,Profile)
    
