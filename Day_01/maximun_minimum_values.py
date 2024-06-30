# Find the maximum and minimum values in a list of numbers

# Prompt the user to enter a list of numbers separated by spaces
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Find the maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)

# Print the results
print(f"The maximum value is {max_value}")
print(f"The minimum value is {min_value}")
