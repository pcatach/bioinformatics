import random
i=input("digite numero do codigo (1,2,3,..)")
file=open("randomico"+i+".txt","w")
a=0
l=["A","C","G","T"]
while a<4639675:
    a+=1
    r=random.randint(0,3)
    file.write(l[r])
file.close()
