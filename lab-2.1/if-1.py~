"""
Program Name: if-1.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Counts the pennies in the user's penny jar and determines its nearness to
    $1.00.
Dates: 2022-09-17 - File created.
"""

# Ask the user for their penny tally
pennies = input("How many pennies in your jar, bucko? ")

# Determine the numberness of the provided input
if pennies.isnumeric() is False:
    # Tell the user that their input was bad
    print("I scoff at your abject destitution. Come back with some more ducats, bum.")
else:
    # Convert input penny amount to dollars
    pennies = int(pennies)
    dollars = pennies / 100
    # Tell them about the contents of their coffers in relation to a dollar
    if dollars == 1:
        print("You have one dollar exactly! You can now buy one sixth of a Big Mac.")
    elif dollars > 1:
        print("You have more than one dollar.\n${:.2f}, to be precise.".format(dollars))
    elif dollars < 1:
        print("You have less than one dollar.\n${:.2f}, to be precise.".format(dollars))
        print("Better than nothing, I suppose.")
    print("That's all, folks!")
