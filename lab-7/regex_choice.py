"""
Program Name: regex_choice.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Validate a float using regex.
Dates: 2022-11-04 - File created.
"""

import re  # compile(), search()


# I picked option 2!!
def main():
    # signed float regex
    float_regex = re.compile(r'''
    ^-?     # signed? maybe!
    (\d+)?  # as many digits as you like
    (\.     # decimal point (optional)
    \d+)?$  # mantissa (optional)
    ''', re.VERBOSE)

    # ask for a float to verify
    print("Please enter a floating-point number.")
    float_search = str(input("$ "))

    # check the string
    float_search_object = float_regex.search(float_search)
    if float_search_object is not None:
        print(f"{float_search} is a valid float! yes!")
    else:
        print("Some huh?")


if __name__ == "__main__":
    main()
