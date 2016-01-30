s = input('s: ')

def skew(s):
	skew = 0
	for letra in s:
		if letra == 'C':
			skew += 1
		elif letra == 'G':
			skew -= 1
	return skew

scores =[]
for i in range(len(s)):
	scores.append( skew(s[:i]))
print  scores.index(max(scores))
