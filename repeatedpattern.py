'''pattern matching problem'''
def main():
    pattern=input()
    genome=input()
    for i in range(len(genome)-len(pattern)+1):
        kmer=""
        for k in range(len(pattern)):
            kmer+=genome[i+k]
        if kmer==pattern:
            print(i,end=' ')

main()
