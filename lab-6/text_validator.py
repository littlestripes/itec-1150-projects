"""
Program Name: text_validator.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Validates a full name given by the user.
Dates: 2022-10-28 - File created.
"""

# words not to be capitalized unless at the beginning of a name string
SPECIAL_WORDS = ["van", "der", "de", "di", "do", "da"]


def validate_name() -> str:
    """
    Validates  and corrects the string passed in according to a set of
    proper noun rules.

    :returns: str, correctly formatted name
    """
    print("Please enter a full name for validation and correction.")
    while True:
        name_str = str(input("$ "))
        # check if name has numbers or at least has a first and last name
        if " " not in name_str:
            print("Try again, a FULL name please.")
            continue
        else:
            # check for digits in the name string using a dummy flag
            if hasdigits(name_str):
                print("No numbers!! Bad!")
                continue
            else:
                break

    # split the input string into a list of name words
    name_words = name_str.split()
    # format all words to ensure no extraneous spaces
    name_words = [word.strip() for word in name_words]
    # and the great big formatted name list comprehension
    new_name_words = [word.capitalize()
                      if word not in SPECIAL_WORDS
                      else word
                      for word in name_words[1:]]
    # first name is always capitalized
    new_name_words.insert(0, name_words[0].capitalize())

    # make a properly formatted name string
    name = " ".join(new_name_words)
    return name


def hasdigits(string: str) -> bool:
    """
    Checks string if it has any digits in it.

    :param string: str, string to be checked for digits
    :returns     : bool, whether or not there are digits
    """
    has_digits = False
    for char in string:
        if char.isdigit():
            has_digits = True

    return has_digits


def main():
    # welcome the user
    print("Welcome to the name validation program.")
    name = validate_name()
    print(f"The full corrected name is: {name}")
    return


main()
