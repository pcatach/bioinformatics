def main():
    spec=input()
    spec=spec.split(' ')
    spectrum=[]
    for i in spec:
        spectrum.append(int(i))

    f=[]
    lista=expand([[]])
    while len(lista)>0:
        lista=expand(lista)    
        lis=lista[:]
        for peptide in lis:
            if consistent(fspectrum(peptide),spectrum) and max(fspectrum(peptide))==max(spectrum):
                ans=[]
                for i in peptide:
                    ans.append(str(i))
                f.append('-'.join(ans))
                lista.remove(peptide)
            elif not consistent(fspectrum(peptide),spectrum) or sum(fspectrum(peptide))>sum(spectrum):
                lista.remove(peptide)

    b=[]
    for k in f:
        if k not in b:
            b.append(k)

    for elem in b:
        print(elem,end=' ')

def fspectrum(peptide):
    #print(peptide, end=' ')
    subpeptides=[]
    for i in range(1,len(peptide)+1):
        for j in range(len(peptide)):
            try:
                if j+i<=len(peptide):
                    l=peptide[j:j+i]
                    subpeptides.append(l)
            except:
                pass
    
    spectrum=[]
    for i in subpeptides:
        spectrum.append(sum(i))
    #print(spectrum)
    return spectrum

def consistent(a,b):
    for i in a:
        if i not in b:
            return False
    return True

def expand(lista):
    table={}
    file=open('integer_mass_table.txt')
    for line in file:
        table[line[0]]=int(line[2:])
    file.close()

    items=[j for j in table.values()]
    extended=[]
    for i in lista:
        for k in items:
            r=i[:]
            r.append(k)
            extended.append(r)
    return extended
    
main()
