#!/usr/local/bin/python3

with open('vocab.txt') as vocab_list:
    entries = [line.rstrip().split(' ', 1) for line in vocab_list]
entries.sort()

with open('sortedVocab.txt', 'w') as output:
    for entry in entries:
        #output.write('{0}\n'.format(' '.join(entry)))
        output.write(' '.join(entry) + '\n')
