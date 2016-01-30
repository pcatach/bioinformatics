def dpchange(money, coins):
    MinNumCoins = [0]*(money+1)
    for m in range(1,money+1):
        MinNumCoins[m] = 10*money
        for i in range(len(coins)):
            if m >= coins[i]:
                if MinNumCoins[m - coins[i]] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - coins[i]] + 1
    return MinNumCoins[money]

data = open('data.txt')

content = data.readlines()

money = int(content[0][:-1])
coins = [ int(a) for a in content[1][:-1].split(',') ]

print dpchange(money,coins)
