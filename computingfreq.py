def NumberToSymbol(number):
    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    elif number == 3:
        return 'T'

def SymbolToNumber(symbol):
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    elif symbol == 'T':
        return 3

def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = index//4
    r = index%4
    PrefixPattern = NumberToPattern(prefixIndex, k-1)
    symbol = NumberToSymbol(r)
    return PrefixPattern + symbol

def PatternToNumber(Pattern):
    if Pattern == '':
        return 0
    symbol = Pattern[-1]
    Pattern = Pattern[:-1]
    return 4*PatternToNumber(Pattern) + SymbolToNumber(symbol)

def ComputingFrequencies(Text, k):
    FrequencyArray = [0]*(4**k)
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] += 1
    return FrequencyArray
'''
Text = raw_input("Digite o texto: ")
k = int(raw_input("Digite k: "))
array = ComputingFrequencies(Text, k)

print ' '.join(str(i) for i in array)
'''
