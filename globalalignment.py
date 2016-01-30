def global_alignment(v, w, scoring_matrix, sigma):

    # Initialize the matrices.
    S = [[0 for repeat_j in xrange(len(w)+1)] for repeat_i in xrange(len(v)+1)]
    backtrack = [[0 for repeat_j in xrange(len(w)+1)] for repeat_i in xrange(len(v)+1)]

    # Initialize the edges with the given penalties.
    for i in xrange(1, len(v)+1):
        S[i][0] = -i*sigma
    for j in xrange(1, len(w)+1):
        S[0][j] = -j*sigma

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoring_matrix[v[i-1]][ w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Initialize the aligned strings as the input strings.
    v_aligned, w_aligned = v, w

    # Get the position of the highest scoring cell in the matrix and the high score.
    i, j = len(v), len(w)
    max_score = str(S[i][j])

    # Backtrack to the edge of the matrix starting at the highest scoring cell.
    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1

    # Prepend the necessary preceeding indels to get to (0,0).
    for repeat in xrange(i):
        w_aligned = insert_indel(w_aligned, 0)
    for repeat in xrange(j):
        v_aligned = insert_indel(v_aligned, 0)

    return max_score, v_aligned, w_aligned

if __name__ == '__main__':
    arq = open("BLOSUM62.txt")
    BLOSUM62 = {}
    for line in arq:
        lista = line.split(" ")
        try:
            BLOSUM62[lista[0]][lista[1]]=int(lista[2][:-1])
        except:
            BLOSUM62[lista[0]] = { lista[1] : int(lista[2][:-1]) }
    arq.close()

    # Read the input data.
    with open('data.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]

    # Get the alignment.
    alignment = global_alignment(word1, word2, BLOSUM62, 5)

    # Print and save the answer.
    print '\n'.join(alignment)
