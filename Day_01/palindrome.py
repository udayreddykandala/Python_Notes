# Check if a given string is a palindrome

def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]


# Prompt the user to enter a string
string = input("Enter a string: ")

# Check if the string is a palindrome and print the result
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
