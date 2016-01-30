'''pattern matching problem w/ mismatches'''
def main():
    pattern=input()
    text=input()
    d=int(input())
    for i in range(len(text)-len(pattern)+1):
        e=0
        for j in range(len(pattern)):
            if text[i:i+len(pattern)][j]!=pattern[j]:
                e+=1
        if e<=d:
            print(i,end=' ')

    
main()
