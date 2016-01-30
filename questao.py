from hamming import hamming
from itertools import product

pattern = "TGCA"
k = 4
d = 3

nei=[]

for p in product('ACGT', repeat = k):
	if hamming(pattern,p)<=d:
		nei.append(p)

print len(nei)
