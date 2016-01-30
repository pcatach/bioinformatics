'''protein translation'''
def main():
    text=input()
    file=open("RNA_codon_table_1.txt")
    content=file.read()
    file.close()
    table={}
    parada=['UAA','UAG','UGA']
    i=0
    while i<len(content):
        table[content[i:i+3]]=content[i+4]
        i+=6
    ans=''
    for j in range(0,len(text),3):
        if text[j:j+3] not in parada:
            ans+=table[text[j:j+3]]
        else:
            j=len(text)
    print(ans)
    
main()
