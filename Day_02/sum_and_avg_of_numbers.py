# Find the sum and average of a list of numbers

# Prompt the user to enter a list of numbers separated by spaces
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

# Calculate the sum
total_sum = sum(numbers)

# Calculate the average
average = total_sum / len(numbers) if numbers else 0

# Print the results
print(f"The sum of the numbers is {total_sum}")
print(f"The average of the numbers is {average}")
