#!/usr/local/bin/python3
import random
import os

NUM_WORST = 10

clear = lambda: os.system('clear')              # Function to clear terminal

with open('vocab.txt', 'r') as vocab_list:
    vocab = [l.rstrip().split(' ', 1) for l in vocab_list]
vocab.sort()

num_words = len(vocab)
num_learned = 0

vocab_copy = vocab
scores = [0] * num_words                # Creates list of 0s, size num_words

while num_words - num_learned > 0:
    clear()
    selection  = random.choice(vocab)
    selection_index = vocab.index(selection)
    word, definition = selection
    definition = definition.strip('"')  # Gets rid of " "

    print(word, "\n\n%d/%d" % (num_learned, num_words))
    response = input()
    if response == "q":
        #quit()
        break
    clear()

    print(word, "-", definition)
    print("\n%d/%d" % (num_learned, num_words))
    response = input()
    if response == "q":
        #quit()
        break
    elif response == "y" or response == "'":
        num_learned += 1
        vocab = vocab[:selection_index] + vocab[selection_index + 1:]
    else:
        scores[selection_index] += 1

clear()
print("Your worst %d words are:" % (NUM_WORST))
for i in range(0, NUM_WORST):
    index_max = scores.index(max(scores))
    word, definition = vocab_copy[index_max]  # Inefficient way to calc
    scores[index_max] = -1                    # multiple maximums
    print(word, "-", definition.strip('"'))
