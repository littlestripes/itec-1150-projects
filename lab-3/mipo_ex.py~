"""
Program Name: mipo_ex.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Exemplify the MIPO structure by calculating the volume of a cube.
Dates: 2022-10-01 - File created.
"""

from sys import exit  # exit()


def main():
    print("This program will give you a boxy little volume, pal")

    while True:
        length, width, height = inputs()
        volume = processing(length, width, height)

        # Final result!
        outputs(volume)

        # Validation loop for the exit prompt
        while True:
            try:
                restart = str(input("Continue? Enter y or n: "))
            except ValueError:
                print("We've gotten this far, pal, throw me a bone!")
                continue

            if restart == "y":
                break
            elif restart == "n":
                print("You probably could've just calculated it with a pencil and\nsome paper, but who am I to judge?")
                exit()
            else:
                print("Quite simple, actually; I need the lowercase letter 'y' or 'n', if you will.")
                continue


def inputs():
    """Takes user input."""
    print("I'm gonna need the length of that there box...")
    length = verify_int_loop()
    print("Now the width...")
    width = verify_int_loop()
    print("And the height...")
    height = verify_int_loop()

    return length, width, height


def verify_int_loop() -> int:
    """Returns input number as an int if it's an int, asks for another if not."""
    while True:
        try:  # check that int is, in fact, an int
            number = int(input("Please enter a whole number: "))
        except ValueError:
            print("A whole number greater than zero, if you please.")
            continue

        if number > 0:  # check that int is positive
            break
        else:
            print("GREATER than zero, if you PLEASE.")
            # Implicit continue

    return number


def processing(length: int, width: int, height: int) -> int:
    return length * width * height


def outputs(volume):
    print(f"The volume of the object is: {volume} cubic units.")


main()
