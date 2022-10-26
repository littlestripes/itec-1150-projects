"""
Program Name: loop-2fun.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Add up some numbers with a loop, but the FUN way!
Dates: 2022-09-23 - File created as loop-2.py.
       2022-10-01 - Modified to conform to the MIPO model.
"""

from sys import exit  # exit()

welcome_msg = """
                        |  _)
  __|  _ \\  |   | __ \\  __| | __ \\   _` |
 (    (   | |   | |   | |   | |   | (   |
\\___|\\___/ \\__,_|_|  _|\\__|_|_|  _|\\__, |
                                   |___/

 __ \\   __| _ \\   _` |  __| _` | __ `__ \\
 |   | |   (   | (   | |   (   | |   |   |
 .__/ _|  \\___/ \\__, |_|  \\__,_|_|  _|  _|
_|              |___/
"""


def welcome(welcome_msg=welcome_msg):  # default arg here refers to the global welcome_msg
    """Welcomes the user with the supplied welcome message."""
    print("Welcome to the\n", welcome_msg)
    print("it also adds up the digits you count! :^)")


def main():
    # Get lower and upper bounds
    lower, upper = inputs()

    # Counting loop
    total = processing(lower, upper)

    # And tell the user about it
    outputs(total)

    while True:
        try:
            choice = str(input("Wanna go again? (y or n) "))
        except ValueError:
            print("I wish not three, but FOUR plagues unto your house!")
            continue

        if choice == "y":
            main()
        elif choice == "n":
            print("Thanks for your time, bub")
            exit()


def inputs():
    """Returns the lower and upper bounds for the counter to use."""
    print("Please enter a small number, 0 or higher.")
    lower = get_positive_int()
    # Loop to ensure the upper bound is higher than the lower bound
    print("And now, a larger number: ")
    while True:
        upper = get_positive_int()

        if upper <= lower:
            print(f"I'll need a bigger number than {upper}, brother-man.")
            print(f"Remember, higher than your lower bound, which is {lower}.")
            continue
        else:
            break

    return lower, upper


def get_positive_int() -> int:
    """Accept a positive integer (or 0) from the user and verify its intness."""
    while True:
        try:
            num = int(input("?> "))
        except ValueError:
            print("I need an integer, compadre.")
            continue

        if num >= 0:
            break
        else:
            print("Gotta be positive, man.")
            continue

    return num


def processing(lower: int, upper: int) -> int:
    """Counts from lower to upper and returns the total."""
    total = 0

    for i in range(lower, upper+1):
        print(i)
        total += i

    return total


def outputs(total):
    """Tell the user what the total ended up being."""
    print(f"The total of all those numbers is {total}.")


welcome()
main()
