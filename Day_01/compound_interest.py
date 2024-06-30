# Calculate the compound interest for a given principal amount, interest rate, and time period

# Prompt the user to enter the principal amount
principal = float(input("Enter the principal amount: "))

# Prompt the user to enter the annual interest rate (as a percentage)
rate = float(input("Enter the annual interest rate (in %): "))

# Prompt the user to enter the time period in years
time = float(input("Enter the time period in years: "))

# Calculate compound interest
compound_interest = principal * (1 + rate / 100) ** time - principal

# Print the result
print(f"The compound interest is {compound_interest:.2f}")
