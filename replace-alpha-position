"""
Title: Replace With Alphabet Position
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
a being 1, b being 2, etc.
"""

def alphabet_position(text):
    list_all = list(filter(lambda x: x > 0, [ord(letter.lower()) - 96 for letter in text]))
    return " ".join([str(num) for num in list_all])
