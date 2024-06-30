# Check if a given string is a pangram

import string


def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())


# Prompt the user to enter a string
sentence = input("Enter a sentence: ")

# Check if the string is a pangram and print the result
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
