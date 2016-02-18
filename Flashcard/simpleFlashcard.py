#!/usr/local/bin/python3
import random
import os

clear = lambda: os.system('clear')

with open('vocab.txt', 'r') as vocab_list:
    vocab = [l.rstrip().split(' ', 1) for l in vocab_list]
vocab.sort()

num_words = len(vocab)
num_learned = 0

while num_words - num_learned > 0:
    clear()
    selection  = random.choice(vocab)
    selection_index = vocab.index(selection)
    word, definition = selection
    definition = definition.strip('"')

    print(word, "\n\n%d/%d" % (num_learned, num_words))
    response = input()
    if response == "q":
        quit()
    clear()

    print(word, "-", definition)
    print("\n%d/%d" % (num_learned, num_words))
    response = input()
    if response == "q":
        quit()
    elif response == "y" or response == "'":
        num_learned += 1
        vocab = vocab[:selection_index] + vocab[selection_index + 1:]

clear()
print("You win!!")
