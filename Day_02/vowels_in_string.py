# Count the number of vowels in a given string

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


# Prompt the user to enter a string
string = input("Enter a string: ")

# Count the vowels and print the result
vowel_count = count_vowels(string)
print(f"The number of vowels in the string is {vowel_count}")
