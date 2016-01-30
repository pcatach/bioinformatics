from operator import neg
def greedysorting(permutation):
    permutation_sequence = []

    # Initialize a list to store all permutations in the transformation to the identity permutation.
    permutation_sequence = []

    # Lambda function to find the index of a given element in the permutation.
    k_index = lambda perm, k: map(abs, perm).index(k)

    # Lambda function to swap and negate the region spanned from index i to index j.
    k_sort = lambda perm, i, j: perm[:i] + map(neg, perm[i:j+1][::-1]) + perm[j+1:]

    # Loop over the permutation to sort it, following the greedy sorting algorithm.
    i = 0
    while i < len(permutation):
        if permutation[i] == i+1:
            i += 1
        else:
            permutation = k_sort(permutation, i, k_index(permutation, i+1))
            permutation_sequence.append(permutation)

    # Note: the approximate reversal distance is the length of the permutation sequence.
    return permutation_sequence

with open('data.txt') as data:
    P = map(int, data.read().strip().lstrip('(').rstrip(')').split())
reversal_list =  greedysorting(P)
reversal_list = ['('+' '.join([['', '+'][value > 0] + str(value) for value in perm])+')' for perm in reversal_list]

with open('resp.txt', 'w') as data:
    data.write('\n'.join(reversal_list))
