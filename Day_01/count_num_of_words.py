# Count the number of words in a given sentence

# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Count the number of words
word_count = len(sentence.split())
letter_count = len(sentence[0])

# Print the result
print(f"The number of words in the sentence is {word_count}")
print(f"The number of letters in the sentence is {letter_count}")
