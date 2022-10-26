"""
Program Name: gas_calc.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Calculate the average miles per gallon and cost of a trip using
    user-provided gas price, miles driven, and gallons burnt.
Dates: 2022-09-06 - File created.
"""

# Ask for input from the user, store values in corresponding variables
# (no checking for valid input, to keep things simple)
miles_driven = float(input("How many miles did you drive? "))
gallons_used = float(input("How many gallons of gas did you use? "))
gas_price = float(input("How much was your gas per gallon? "))

# Calculate mpg and trip cost
avg_mpg = miles_driven / gallons_used
trip_cost = gallons_used * gas_price

# Display formatted results to the user
print("\nHere are some fun facts about your trip!")
print("{:<20}{:>6.2f}".format("MPG:", avg_mpg))
print("{:<20}{:>6.2f}".format("Trip Cost (in $):", trip_cost))
