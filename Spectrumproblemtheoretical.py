'''Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
     Input: An amino acid string Peptide.
     Output: Cyclospectrum(Peptide).'''
def main():
    peptide=raw_input()

    table={}
    table['0']=0
    file=open('integer_mass_table.txt')
    for line in file:
        table[line[0]]=int(line[2:])
    file.close()

    subpeptides=[peptide]
    peptide+=peptide[:-1]
    for i in range(1,len(peptide)//2+1):
        for j in range(len(peptide)//2+1):
            subpeptides.append(peptide[j:j+i])


    spectrum=[0]
    for i in subpeptides:
        if i not in spectrum:
            x=0
            for j in i:
                x+=table[j]
            spectrum.append(x)
            
    for i in sorted(spectrum,key=int):
        print i, " ",
main()

