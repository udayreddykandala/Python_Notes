# Concatenate a list of names into a single string separated by spaces

# Prompt the user to enter a list of names separated by spaces
names = input("Enter names separated by spaces: ").split()

# Concatenate the names
concatenated_names = ' '.join(names)

# Print the result
print(f"The concatenated names are: {concatenated_names}")
