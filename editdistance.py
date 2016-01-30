def edit_distance(v,w):
    '''Returns the edit distance of strings v and w.'''
    from numpy import zeros

    # Initialize matrix M.
    M = zeros((len(v)+1,len(w)+1), dtype=int)
    for i in range(1,len(v)+1):
        M[i][0] = i
    for j in range(1,len(w)+1):
        M[0][j] = j

    # Compute each entry of M.
    for i in xrange(1,len(v)+1):
        for j in xrange(1,len(w)+1):
            if v[i-1] == w[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j]+1, M[i][j-1]+1, M[i-1][j-1]+1)

    # Print and save the desired edit distance.
    return M[len(v)][len(w)]

if __name__ == '__main__':

    # Read the input data.
    with open('data.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]

    # Get the edit distance.
    e_dist = edit_distance(word1, word2)

    # Print and save the answer.
    print str(e_dist)
