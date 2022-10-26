"""
Program Name: color_mixer.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Mixes two primary colors that the user provides.
Dates: 2022-09-17 - File created.
"""

# List of primary colors to choose from
options = ["red", "yellow", "blue"]

# Introduce the user to the program's aim
print("What happens when you mix two different primary colors?")

# Accept first color choice from the user
while True:
    first_color = str(input("Enter a primary color - red, yellow, or blue: "))
    # If the color selection is in the list of options, break the loop
    if first_color in options:
        # Ensure the first color can't be chosen again by removing it from the
        # list of options
        options.remove(first_color)
        break
    else:
        print("Please select from the available options.")

# And again for the second one
while True:
    second_color = str(input("Enter another primary color, different from the first: "))
    if second_color in options:
        break
    elif second_color == first_color:
        print("Enter a DIFFERENT color from the first, PLEASE.")
    else:
        print("Please select from the available options.")

# Store the user's choices in a sorted list
choices = [first_color, second_color]
choices.sort()

# Check the choices list against presorted results
if choices == ["red", "yellow"]:
    print("Red and yellow make orange! Nice!")
elif choices == ["blue", "yellow"]:
    print("Yellow and blue make green! Nice!")
else:
    # Purple case if neither orange nor green
    print("Red and blue make purple! Nice!")

# Say bye bye
print("Thanks for playing.")
