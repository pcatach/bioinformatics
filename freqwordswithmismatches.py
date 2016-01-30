def main():
    text=input()
    k=int(input())
    d=int(input())
    l={}
    for i in range(len(text)-k+1):
        if text[i:i+k] in l:
            l[text[i:i+k]]+=1
        else:
            #print(i)
            addkmer(text[i:i+k],l,d)
    max_freq=max(l.values())
    ans=[kmer for kmer, freq in l.items() if freq==max_freq]
    print(' '.join(ans))

def addkmer(kmer,l,d):
    mismatch=equal=False
    if len(l.keys())==0:
        l[kmer]=1
    else:
        toadd={}
        for i in l.keys():
            e=0
            for j in range(len(i)):
                if i[j]!=kmer[j]:
                    e+=1
            if e<=d and i!=kmer:
                l[i]+=1
                a=l[i]
                toadd[kmer]=a
                mismatch=True
            elif i==kmer:
                l[i]+=1
                equal=True
            else:
                toadd[kmer]=1
        if mismatch:
            l[kmer]=dict(list(l.items())+list(toadd.items()))
        if not equal:
            l[kmer]=1
'''    toprint=[(f,num) for f,num in l.items() if num>1]
    print(toprint)'''
main()
