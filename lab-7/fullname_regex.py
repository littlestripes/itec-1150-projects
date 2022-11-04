"""
Program Name: fullname_regex.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Determines whether or not input text is a full name.
Dates: 2022-11-04 - File created.
"""

import re  # compile(), search()


def main():
    # regex to use
    name_regex = re.compile(r'''
    ^[a-zA-Z] # first name
    [\s|-]    # separator (could be space or hyphen)
    [a-zA-Z]  # middle name
    [\s|-]    # separator
    [a-zA-Z]$ # last name
    ''', re.VERBOSE)

    # ask user for string to search
    print("Enter full name in this format - first middle last")
    name_source = str(input("$ "))
    name_search_object = name_regex.search(name_source)


if __name__ == "__main__":
    main()
