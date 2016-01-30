from collections import defaultdict
from string import maketrans

def rev_comp(nucleic_acid):
    '''Returns the reverse complement of a given DNA strand.'''
    nucleotide = 'ATCG'
    complement = 'TAGC'
    transtab = maketrans(nucleotide, complement)

    return nucleic_acid.translate(transtab)[::-1].lstrip()


def shared_kmers(k, dna1, dna2):
    '''Returns a list of positions for shared k-mers (up to reverse complement) in dna1 and dna2.'''

    # Store the starting index of all k-mers from dna1 in a dictionary keyed to the k-mer.
    dna1_dict = defaultdict(list)
    for i in xrange(len(dna1) - k + 1):
        dna1_dict[dna1[i:i+k]].append(i)

    # Check k-mers in dna2 against those in dna1, add matching index pairs to a set to remove possible duplicate entries.
    shared_kmer_indices = set()
    for j in xrange(len(dna2) - k + 1):
        shared_kmer_indices |= set(map(lambda x: (x,j), dna1_dict[dna2[j:j+k]]))
        shared_kmer_indices |= set(map(lambda x: (x,j), dna1_dict[rev_comp(dna2[j:j+k])]))

    return shared_kmer_indices


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('data.txt') as input_data:
        k = int(input_data.readline().strip())
        dna1, dna2 = [line.strip() for line in input_data.readlines()]

    # Get the shared kmers.  Sorting doesn't add significant time and makes the result more readable.
    shared_kmer_indices = map(str, sorted(shared_kmers(k, dna1, dna2)))

    # Print and save the answer.
    print '\n'.join(shared_kmer_indices)
    with open('resp.txt', 'w') as output_data:
        output_data.write('\n'.join(shared_kmer_indices))

main()
