"""
Lisa Mays
08/20/2021
Discussion 1
This program will calculate sales tax on a purchase using user inputted values for
the amount spent and the tax rate.
"""

# Welcome
print("Welcome to the Tax Calculator.")

# Prompt for the tax rate
taxrate = float(input("Please enter your tax rate as a decimal (i.e. .06): "))

# Prompt for the purchase amount
purchaseamount = float(input("Please enter the total purchase amount: $"))

# Calculate the tax rate by multiplying the tax rate times the purchase amount
taxcharged = (purchaseamount * taxrate)

#Calculate the total cost of the purchase plus the tax amount
totalcharged = (purchaseamount + taxcharged)

#Display the results
print('Your tax amount is: $',taxcharged, ' on your purchase of $',purchaseamount,\
' @ ',taxrate,'%' ' for a total purchase of: $',totalcharged)
