import sys
def lcsbacktrack(v,w):
    s = [ [0]*len(w) for i in range(len(v))  ]

    for i in range(1,len(v)):
        for j in range(1,len(w)):
            if v[i] == w[j]:
                s[i][j] = s[i-1][j-1] + 1
            else:
                s[i][j] = max(s[i-1][j], s[i][j-1]) 
    return s

def outputlcs(S, v, w):
    lcs = ''
    i = len(v)
    j = len(w)
    while i > 0  and j > 0:
        if S[i][j] == S[i-1][j]:
            i = i-1
        elif S[i][j] == S[i][j-1]:
            j = j-1
        else:
            i = i-1
            j = j-1
            lcs += v[i]
    return lcs

arq = open('data.txt')
content = arq.readlines()
s = content[0] if len(content[0])<=len(content[1]) else content[1]
t = content[1] if s == content[0] else content[0]
S = lcsbacktrack(s, t)

print ''.join(reversed(outputlcs(S, s, t)))
