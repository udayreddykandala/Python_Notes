# Convert a given number of days into years, weeks, and days

# Prompt the user to enter the number of days
days = int(input("Enter the number of days: "))

# Calculate the number of years, weeks, and remaining days
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

# Print the results
print(f"{days} days is equal to {years} years, {weeks} weeks, and {remaining_days} days.")
