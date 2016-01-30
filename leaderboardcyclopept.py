'''LEADERBOARDCYCLOPEPTIDESEQUENCING.

Input: Integer N and a collection of integers Spectrum.

Output: LeaderPeptide after running LEADERBOARDCYCLOPEPTIDESEQUENCING(Spectrum, N).'''

from heapq import nlargest as nlargest

def main(spec,n):
    leaderboard=[[]]
    leaderpeptide=[]
    while len(leaderboard)>0:
        leaderboard=expand(leaderboard)
        iterate=leaderboard[:]
        
        for peptide in iterate:
            if sum(peptide)==spec[-1]:
                if score(peptide,spec)>score(leaderpeptide,spec):
                    leaderpeptide=peptide


            elif sum(peptide)>spec[-1]:
                leaderboard.remove(peptide)

        leaderboard=cut(leaderboard,spec,n)
        print(leaderpeptide,len(leaderboard))

    anslist=[]
    for i in leaderpeptide:
        anslist.append(str(i))
    print('-'.join(anslist))


def score(peptide,refspectrum):
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

    s=0
    for i in spectrum:
        if i in refspectrum:
            s+=1
    return s
    
    

def cut(leaderboard,spec,n):
    
    scorelist=[]
    #crio uma lista com os scores de cada item da leaderboard
    for i in leaderboard:
        scorelist.append(score(i,spec))
    
    new=[]
    #crio uma lista com os items em leaderboard que tem score maior que n
    

    for k in range(len(scorelist)):
        if scorelist[k] in nlargest(n,scorelist):
            new.append(leaderboard[k])
    return new



def expand(leaderboard):
    table={}
    file=open('integer_mass_table.txt')
    for line in file:
        table[line[0]]=int(line[2:])
    file.close()

    items=[j for j in table.values()]
    extended=[]
    for i in leaderboard:
        for k in items:
            r=i[:]
            r.append(k)
            extended.append(r)
    return extended




N=int(input())
S=input()
Spec=S.split(" ")
Spectrum=[]
for i in Spec:
    Spectrum.append(int(i))
main(Spectrum,N)
