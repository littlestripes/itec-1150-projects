"""
Program Name: feedback_collector.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Gather and store feedback phrases for students using an LMS.
Dates: 2022-10-28 - File created.
"""

import sys  # exit


def main():
    print("Welcome to the feedback generator, didact.")
    while True:
        feedback_str = inputs()
        feedback_list = processing()
        outputs(feedback_list)
        # confirmation loop
        print("Care to go again?")
        while True:
            command = str(input("$ "))
            if command == "y":
                break
            elif command == "n":
                print("Thanks for coming, compadre.")
                sys.exit()
            else:
                print("Some huh?")


def inputs() -> str:
    """
    Ask the user to enter feedback phrases separated by an
    exclamation mark (!).

    :returns: str, a corrected string of feedback phrases
    """


def processing():
    pass


def outputs():
    pass


main()
