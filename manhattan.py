def manhattan(n, m, down, right):
    s = []
    for i in range(n+1):
        s.append([ 0 for j in range(m+1) ])

    for i in range(1,n+1):
        s[i][0] = s[i-1][0] + down[i-1][0]
    for j in range(1,m+1):
        s[0][j] = s[0][j-1] + right[0][j-1]

    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max([ s[i-1][j] + down[i-1][j] , s[i][j-1] + right[i][j-1] ])

    return s[n][m]


data = open('data.txt')
content = data.readlines()
data.close()

n = int(content[0][:-1].split(' ')[0])
m = int(content[0][:-1].split(' ')[1])

down = []

for i in range(n):
    string = content[1:][i]
    down.append([ int(x) for x in  string[:-1].split(' ')  ])

right = []

for i in range(n+1):
    string = content[n+2:][i]
    right.append([ int(x) for x in string[:-1].split(' ')  ])

print manhattan(n,m,down,right)
