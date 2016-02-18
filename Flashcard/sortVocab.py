#!/usr/local/bin/python3

# Read in vocab.txt and store as list
with open('vocab.txt') as vocab_list:
    entries = [line.rstrip().split(' ', 1) for line in vocab_list]
entries.sort()

# Write the sorted vocab list to file
with open('sortedVocab.txt', 'w') as output:
    for entry in entries:
        #output.write('{0}\n'.format(' '.join(entry)))
        output.write(' '.join(entry) + '\n')
