'''the minimum skew problem'''
def main():
    genome=input()
    ans=[]
    skewList=skew(genome)
    minim=min(skewList)
    for l in range(len(genome)-1):
        if minimSkew(skewList,l,minim)==True:
            ans.append(l)
    print(ans)

def skew(genome):
    skewList=[0]
    c=g=0
    for i in range(len(genome)):
        if genome[i]=='C':
            c+=1
        if genome[i]=='G':
            g+=1
        skewList.append(g-c)
    return skewList

def minimSkew(list,l,minim):
    if list[l]==minim:
        return True
    return False
main()
