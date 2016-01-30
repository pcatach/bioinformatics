'''Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
Input: A DNA string Text and an amino acid string Peptide.
Output: All substrings of Text encoding Peptide (if any such substrings exist).'''
def main():

    file=open("Bbrevis.txt")
    text1=file.read()    
    file.close()
    print("arquivo lido")
    #text1=input()
    peptide=input()
    text2=''
    for i in range(len(text1)):
        if text1[i]=='T':
            text2+='U'
        else:
            text2+=text1[i]
   
        
    #this list will hold every possible substring of 3*len(peptide)-mers that is present on text
    substrings=get_subs(text2,3*len(peptide))

    file=open("RNA_codon_table_1.txt")
    content=file.read()
    file.close()
    table={}
    i=0
    while i<len(content):
        table[content[i:i+3]]=content[i+4]
        i+=6
    table['UAA']=table['UAG']=table['UGA']='0'

    print("carregando")
    
    for s in substrings:
        if encode(s,peptide,table) or encode(reverse(s),peptide,table):
            v=''
            for i in range(len(s)):
                if s[i]=='U':
                    v+='T'
                else:
                    v+=s[i]
            print(v)
            
    

def get_subs(p,k):
    '''this function gets a text p and returns every pattern with k letters in it'''
    subs=[]
    for i in range(len(p)-k+1):
        subs.append(p[i:i+k])
    return subs


def encode(s,peptide,table):

    encoded=''
    for i in range(0,len(s),3):
        encoded+=table[s[i:i+3]] 
    if encoded==peptide:
        return True
    else:
        return False

def reverse(pattern):
    cr=""
    for letter in pattern:
        if letter=="A":
            cr+="U"
        if letter=="C":
            cr+="G"
        if letter=="G":
            cr+="C"
        if letter=="U":
            cr+="A"
    cr=Reverse(cr)
    return cr

def Reverse(text):
    text2=""
    for i in range(len(text)-1,-1,-1):
        text2+=text[i]
    return text2

main()
