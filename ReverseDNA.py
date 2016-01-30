def Reverse(text):
    text2=""
    for i in range(len(text)-1,-1,-1):
        text2+=text[i]
    return text2


text=input("Digite o DNA: ")
cr=""
for letter in text:
    if letter=="A":
        cr+="T"
    if letter=="C":
        cr+="G"
    if letter=="G":
        cr+="C"
    if letter=="T":
        cr+="A"
cr=Reverse(cr)
print("complemento reverso:",cr)
