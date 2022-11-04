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
    float_regex = re.compile('''
    ^-?     # signed? maybe!
    (\d+)   # as many digits as you like
    (\.     # decimal point (optional)
    \d+)?$  # mantissa (optional)
    ''', re.VERBOSE)


if __name__ == "__main__":
    main()
