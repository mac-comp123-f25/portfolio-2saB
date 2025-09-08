# Define a variable called money to hold the initial money amount in cents, eg, 732 for $7.32.  Then, create a series of Python statements that calculate and print how to give change for the money value, in dollars, quarters, dimes, nickels, and pennies. The best solution will use integer division and the remainder operation.
money = 732  # Example: $7.32

print("Making change for", money, "cents:")

# Dollars
dollars = money // 100
money = money % 100

# Quarters
quarters = money // 25
money = money % 25

# Dimes
dimes = money // 10
money = money % 10

# Nickels
nickels = money // 5
money = money % 5

# Pennies
pennies = money

# Print results
print(" Dollars:", dollars)
print(" Quarters:", quarters)
print(" Dimes:", dimes)
print(" Nickels:", nickels)
print(" Pennies:", pennies)
