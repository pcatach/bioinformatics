def Count(list,pattern):
    num=0
    j=0
    while j<len(list):
       if pattern==list[j]:
            num+=1
       j+=1 
    return num

def GenList(t,k):
    text=""
    n=len(t)-len(t)%k
    for i in range(n):
        if i%k!=0 or i==0:
            text+=t[i]
        else:
            text+=":"+t[i]
    list=text.split(":")    
    return list

def main(t,k,s):
    kmers=[]
    kmersn=[]
    list=[]
    i=1
    for a in range(k):
        list.extend(GenList(t,k))
        t=t[i:]
    nlist=[]
    for elem in list:
        n=Count(list,elem)
        nlist.append(n)
    for i in range(len(list)):
        if nlist[i]>=s:
            kmers.append(list[i])
    return(set(kmers))


Genome=input()
k=int(input())
L=int(input())
t=int(input())
ans=[]
for i in range(len(Genome)-L+1):
    view=Genome[i:i+L]
    ans.extend(main(view,k,t))
ans=set(ans)
for a in ans:
    print(a, end=" ")
