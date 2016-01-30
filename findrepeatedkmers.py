def main():
    arq=input("File name: ")
    n=int(input("n for n-mers: "))
    arq2=input("output to: ")
    alphabet=input("alphabets [x/y/z] (to get repeated kmers enter 'xy'): ")

    try:
        file=open(arq)
    except:
        print("File not found!")
        return

    seq=file.read()
    file.close()

    S=[]
    for i in range(0,len(seq),n):
        S.append(seq[i:i+n])

    
    B1=binary(S,alphabet[0])
    B2=binary(S,alphabet[1])


    
    D1=[]
    D2=[]
    for elem in B1:
        decimal=int(elem,2)
        D1.append(decimal)

    for elem in B2:
        decimal=int(elem,2)
        D2.append(decimal)
    
    C=[]
    for i in range(len(D1)):
        coordinate=[]
        coordinate.append(D1[i])
        coordinate.append(D2[i])
        C.append(coordinate)
        
    m=matrix(C,int('1'*n,2))
    
    find_repeat(C,n)

    create_pbm(m,arq2)
    print("concluded.")
    return

def find_repeat(C,n):
    d={}
    for elem in C:
        new=''
        a=bin(elem[0])[2:]
        b=bin(elem[1])[2:]
        for i,j in zip(a,b):
            if i=='1' and j=='1':
                new+='G'
            if i=='0' and j=='1':
                new+='T'
            if i=='1' and j=='0':
                new+='A'
            else:
                new+='C'
        if new in d:
            d[new]+=1
        else:
            d[new]=1
        
    print("The %d -mers with more repetitons are:" %(n), end=' ')
    max_freq=max(d.values())
    ans=[kmer for kmer, freq in d.items() if freq == max_freq]
    print(' '.join(ans))

    

def matrix(C,dim):
    print("creating data...")
    m=[]
    for i in range(dim):
        m.append(['0']*dim)
    for elem in C:
        m[elem[0]-1][elem[1]-1]='1'
    return m
            
    
def binary(seq,alphab):
    B=[]
    if alphab=='x':
        for elem in seq:
            num=''
            for letter in elem:
                if letter=='A' or letter=='G':
                    num+='1'
                else:
                    num+='0'
            B.append(num)
    if alphab=='y':
        for elem in seq:
            num=''
            for letter in elem:
                if letter=='T' or letter=='G':
                    num+='1'
                else:
                    num+='0'
            B.append(num)
    if alphab=='z':
        for elem in seq:
            num=''
            for letter in elem:
                if letter=='A' or letter=='T':
                    num+='1'
                else:
                    num+='0'
            B.append(num)
    return B

def create_pbm(matrix, file):
    print("outputing to pbm file...")
    output=open(file,'w')
    output.write("P1\n"+str(len(matrix))+" "+str(len(matrix))+"\n")
    for line in matrix:
        output.write(''.join(line)+"\n")
    output.close()
    
    
    

main()

