def main():
    text=input()
    peptide=input()
    size=len(peptide)
    #construcao da tabela
    file=open("RNA_codon_table_1.txt")
    content=file.read()
    file.close()
    content2=''
    for l in content:
        if l=='U':
            content2+='T'
        else:
            content+=l
    table={}
    print(content)
    print(content2)
    parada=['TAA','TAG','TGA']
    i=0
    while i<len(content2):
        table[content2[i:i+3]]=content2[i+4]
        i+=6
    for j in range(0,len(text),3):
        encoded=''
        seq=''
        for k in range(size):
            encoded+=table[text[j+(k)*3:j+3*(k+1)]]
            seq+=text[j+(k)*3:j+3*(k+1)]
        if peptide==encoded:
            print(seq)
    

main()
