from hamming import hamming

def apc(text, pattern, d):
    count = 0
    for i in range( len(text) - len(pattern) + 1 ):
        pattern1 = text[i:i+len(pattern)]
        if hamming(pattern, pattern1) <= d:
            count += 1
    return count
'''
text = raw_input("Digite text: ")
pattern = raw_input("Digite pattern: ")
d = int(raw_input("Digite f: "))
print apc(text, pattern, d)
'''
