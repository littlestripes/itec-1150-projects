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
        try:
            feedback_str = inputs()
        # didn't have time to raise a specific error for each thing that could
        # go wrong, sorry :^/
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        feedback_list = processing(feedback_str)
        outputs(feedback_list)
        print("Thanks for your sumptuous contribution.")
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

    :returns          : str, a corrected string of feedback phrases
    :raises ValueError: when the string doesn't satisfy the conditions
                        i.e. doesn't contain "!", no spaces, etc.
    """
    print("Please enter feedback phrases separated with an exclamation mark (!).")
    feedback_str = str(input("$ "))
    # validate
    if "!" not in feedback_str:
        raise ValueError
    # now to format the input
    feedback_words = feedback_str.split()
    # get rid of extraneous spaces
    feedback_words = [feedback.strip() for feedback in feedback_words]
    # and return corrected string
    return " ".join(feedback_words)


def processing(feedback_str: str) -> list:
    """
    Split feedback_str into a list of feedback phrases and format them.

    :param feedback_str: str, string to be formatted into a list
    :returns           : list, list of formatted feedback phrases
    """
    feedback_list = feedback_str.split("!")
    # there's always a space at the end of the list, pop that sucker
    feedback_list.pop(-1)
    # strip and capitalize, again? shouldn't fixing "common errors"
    # be done here in processing()?
    feedback_list = [feedback.strip().capitalize()
                     for feedback in feedback_list]
    # add "!" back to each phrase and return
    feedback_list = [f"{feedback}!" for feedback in feedback_list]
    return feedback_list


def outputs(feedback_list: list):
    """
    Display the feedback phrases to the user.

    :param feedback_list: list, formatted feedback phrases
    """
    print("Here are your phrases:")
    for idx, feedback in enumerate(feedback_list):
        print(f"{idx + 1}: {feedback}")


main()
