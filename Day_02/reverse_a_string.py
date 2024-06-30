# Create a function to reverse a given string

def reverse_string(s):
    return s[::-1]


# Prompt the user to enter a string
string = input("Enter a string: ")

# Reverse the string and print the result
reversed_string = reverse_string(string)
print(f"The reversed string is: {reversed_string}")
