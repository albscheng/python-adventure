#!/usr/local/bin/python3
import random
import os

clear = lambda: os.system('clear')

with open('vocab.txt', 'r') as vocab_list:
    vocab = [l.rstrip().split(' ', 1) for l in vocab_list]
vocab.sort()

while True:
    clear()
    word, definition = random.choice(vocab)
    definition = definition.strip('"')

    print(word)
    response = input()
    if response == "q":
        quit()
    clear()

    print(word, "-", definition)
    response = input()
    if response == "q":
        quit()


