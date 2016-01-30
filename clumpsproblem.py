'''clump finding problem'''
def main():
    genome=input()
    k=int(input())
    L=int(input())
    t=int(input())
    kmers=[]
    for a in range(len(genome)-L):
        view=genome[a:a+L]
        kmers.extend(findPatterns(view,k,t))
    print(' '.join(set(kmers)))
        
def findPatterns(text,k,t):
    d={}
    for i in range(len(text)-k+1):
        kmer=text[i:i+k]
        if kmer in d:
            d[kmer]+=1
        else:
            d[kmer]=1
    ans=[kmer for kmer, freq in d.items() if freq>=t]
    return ans

main()
