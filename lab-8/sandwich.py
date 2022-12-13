"""
Program Name: sandwich.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Tabulate the costs of sandwiches with various ingredients.

    forgive me, there's probably a much easier way to do everything I did here
Dates: 2022-12-13 - File created.
"""

import sys                  # exit()
import pyinputplus as pyip  # inputStr(), inputNum()

# sandwich ingredients and their prices
INGREDIENTS = {
    "breads": {
        "wheat": 0.0,
        "white": 0.0,
        "sourdough": 0.5
    },
    "proteins": {
        "chicken": 2.5,
        "turkey": 2.5,
        "ham": 3.0,
        "bison": 5.0,
        "endangered species surprise!": 15.0,
        "tofu": 7.5
    },
    "cheeses": {
        "cheddar": 1.5,
        "swiss": 1.5,
        "mozzarella": 1.0,
        "american": -2.0,  # this is on purpose, you deserve a discount to eat this
    },
    "other": {
        "mayo": 0.25,
        "mustard": 0.25,
        "lettuce": 0.3,
        "tomato": 0.3
    }
}

# for pyinputplus compatibility (mainly with inputMenu()), it needs
# a standard, garden-variety iterable to work with; a dict_keys object
# doesn't cut it
BREADS = list(INGREDIENTS["breads"].keys())
PROTEINS = list(INGREDIENTS["proteins"].keys())
CHEESES = list(INGREDIENTS["cheeses"].keys())
OTHER = list(INGREDIENTS["other"].keys())
# and this is for overengineering purposes
ALL_INGREDIENTS_DICT = {**INGREDIENTS["breads"],
                        **INGREDIENTS["proteins"],
                        **INGREDIENTS["cheeses"],
                        **INGREDIENTS["other"]}


def main():
    sandwiches = inputs()  # populate a dict with book names and prices
    sandwiches, total = processing(sandwiches)  # use said prices to get mean and total
    outputs(sandwiches, total)  # format for user-friendly use

    # restart loop
    while True:
        # restart prompt, accepts str and cannot be empty
        restart = pyip.inputYesNo(prompt="Need more sammies? (y or n): ")
        if restart == "yes":
            main()
        elif restart == "no":
            print("Thanks for your time.")
            sys.exit()
        else:
            print("Some huh?")


def inputs() -> list:
    """
    Returns a list of sandwiches in this format:

    [[``list``, ``of``, ``ingredients``], [``...``, ``...``], ...]
    """
    # prompts user for number of sandwiches to order, at least 1
    num_sandwiches = pyip.inputInt(min=1, prompt="How many heros? ")

    sandwiches = [list() for _ in range(num_sandwiches)]
    # populate the empty list with sandwiches
    for sandwich in range(num_sandwiches):
        # ask for bread type using INGREDIENTS["breads"] as choices
        bread = pyip.inputMenu(BREADS, prompt="\nPick a bread!\n")
        sandwiches[sandwich].append(str(bread))
        # same deal for protein
        protein = pyip.inputMenu(PROTEINS, prompt="\nPick a protein!\n")
        sandwiches[sandwich].append(str(protein))
        # and a confirmation for cheese before we put any on
        wants_cheese = pyip.inputYesNo(prompt="\nWant cheese?\n")
        if wants_cheese == "yes":
            cheese = pyip.inputMenu(CHEESES, prompt="\nPick a cheese!\n")
            sandwiches[sandwich].append(str(cheese))
        # then a series of yes/no for other condiments
        wants_mayo = pyip.inputYesNo(prompt="\nWant mayo?\n")
        if wants_mayo == "yes":
            sandwiches[sandwich].append("mayo")
        wants_mustard = pyip.inputYesNo(prompt="Want mustard?\n")
        if wants_mustard == "yes":
            sandwiches[sandwich].append("mustard")
        wants_lettuce = pyip.inputYesNo(prompt="Want lettuce?\n")
        if wants_lettuce == "yes":
            sandwiches[sandwich].append("lettuce")
        wants_tomato = pyip.inputYesNo(prompt="Want tomato?\n")
        if wants_tomato == "yes":
            sandwiches[sandwich].append("tomato")

        if sandwich + 1 != num_sandwiches:
            print("\nNext sammy!")

    return sandwiches


def processing(sandwiches: list) -> list:
    """
    Returns a list of dicts with total prices and list of ingredients
    for the sandwiches list supplied.
    """
    sandwich_list = list()
    for sandwich in sandwiches:
        sandwich_dict = {
            "ingredients": dict(),
            "total_price": 0.0
        }
        # construct a dict of ingredients and their prices based on the list
        # of ingredients passed in
        sandwich_dict["ingredients"] = dict.fromkeys(sandwich)
        for ingredient in sandwich_dict["ingredients"]:
            sandwich_dict["ingredients"][ingredient] = ALL_INGREDIENTS_DICT[ingredient]
        # include the total price of the sandwich
        sandwich_dict["total_price"] = sum(sandwich_dict["ingredients"].values())
        sandwich_list.append(sandwich_dict)

    # calculate total price of all sandwiches
    total = sum([sandwich["total_price"] for sandwich in sandwich_list])

    return sandwich_list, total


def outputs(sandwiches: list, total: float):
    """Outputs the data in a beautiful, meaningful table."""
    print("\nVal's Sammy Kingdom\n===================")
    print("Sandwiches:\n")
    for idx, sandwich in enumerate(sandwiches):
        print(f"Sandwich #{idx + 1}:")
        print("{:<30}{:>8}".format("Ingredient", "Price"))
        for ingredient, price in sandwich["ingredients"].items():
            print("{:<30}${:>8.2f}".format(ingredient, price))
        print("{:<30}${:>8.2f}\n".format(f"Sandwich #{idx + 1} Total:", sandwich["total_price"]))
    print("\n{:<30}${:>8.2f}\n".format("Grand Total", total))


if __name__ == "__main__":
    print("Welcome to Val's Sammy Kingdom!")
    main()
