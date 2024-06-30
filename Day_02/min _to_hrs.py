# Convert a given number of minutes into hours and minutes

# Prompt the user to enter the number of minutes
total_minutes = int(input("Enter the number of minutes: "))

# Calculate the number of hours and remaining minutes
hours = total_minutes // 60
minutes = total_minutes % 60

# Print the results
print(f"{total_minutes} minutes is equal to {hours} hours and {minutes} minutes.")
