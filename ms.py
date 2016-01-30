#!/usr/bin/env python

from itertools import product

def HammingDistance(str1, str2):
	diffs = 0
	for ch1, ch2 in zip(str1, str2):
		if ch1 != ch2:
			diffs += 1
	return diffs

def motif_score(pattern, motif):
	'''Returns the score of d(pattern, motif).'''
	return min([HammingDistance(motif[i:i+len(pattern)], pattern) for i in range(len(motif)-len(pattern)+1)])

with open('questao6') as input_data:
	k = int(input_data.readline())
	dna_list = [line.strip() for line in input_data.readlines()]

# Initialize the best pattern score as one greater than the maximum possible score.
best_pattern = [k*len(dna_list) + 1, None]

# Check the scores of all k-mers.
for pattern in product('ACGT', repeat=k):
	current_score = sum([motif_score(''.join(pattern),dna) for dna in dna_list])
	if current_score < best_pattern[0]:
		best_pattern = [current_score, ''.join(pattern)]

# Print and save the answer.
print best_pattern[1]
