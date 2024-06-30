# Count the number of words in a given sentence

# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Count the number of words
word_count = len(sentence.split())
# Count the number of letters
letter_count = sum(c.isalpha() for c in sentence)

# Print the result
print(f"The number of words in the sentence is {word_count}")
print(f"The number of letters in the sentence is {letter_count}")
