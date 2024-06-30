# Find the sum of all positive numbers in a list of integers

# Prompt the user to enter a list of numbers separated by spaces
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calculate the sum of all positive numbers
positive_sum = sum(num for num in numbers if num > 0)

# Print the result
print(f"The sum of all positive numbers is {positive_sum}")
