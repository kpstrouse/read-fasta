import sys

def read_fasta(filename):
    """Reads a FASTA sequence from a file and returns it"""
    sequence = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            # Append to the last sequence
            sequence = sequence + line
    f.close()
    return sequence

# print friendly message if used incorrectly

if len(sys.argv) < 2:
    print('Usage:', sys.argv[0], '<sequence.fa>')
    exit(1)

# use file name from command line

print(read_fasta(sys.argv[1]))
