def hamming(s1,s2):
	score = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			score += 1
	return score
'''
s1 = raw_input("digite texto 1: ")
s2 = raw_input("digite texto 2: ")
print hamming(s1,s2)
'''
