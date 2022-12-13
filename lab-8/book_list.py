"""
Program Name: book_list.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Tabulate the costs of a series of books.
Dates: 2022-10-05 - File created.
       2022-12-13 - Updated to use pyinputplus input functions.
"""

import sys                  # exit()
import pyinputplus as pyip  # inputStr(), inputNum()


def main():
    books = inputs()  # populate a dict with book names and prices
    total, average = processing(books.values())  # use said prices to get mean and total
    outputs(books, total, average)  # format for user-friendly use

    # restart loop
    while True:
        # restart prompt, accepts str and cannot be empty
        restart = pyip.inputStr(prompt="Need more books? (y or n): ")
        if restart == "y":
            main()
        elif restart == "n":
            print("Thanks for your time.")
            sys.exit()
        else:
            print("Some huh?")


def inputs() -> dict:
    """Returns a dict of book names and prices."""
    # prompts user for number of books to tally, at least 1
    num_books = pyip.inputNum(min=1, prompt="How many books? ")

    books = dict()
    # populate the empty dict with book details
    for book in range(1, num_books+1):
        # prompts user for the name of the given book
        book_name = pyip.inputStr(prompt=f"Name of book {book}: ")
        # prompts user for price of said book, min and max params specify that
        # it should be a float
        book_price = pyip.inputNum(min=0.01,
                                   max=100.00,
                                   prompt="Please enter the cost of the book: ")
        books[book_name] = book_price

    return books


def processing(book_prices: list) -> (float, float):
    """Returns total and mean prices for the price list supplied."""
    book_price_avg = sum(book_prices) / len(book_prices)
    return sum(book_prices), round(book_price_avg, 2)


def outputs(books: dict, total: float, avg: float):
    """Outputs the data in a beautiful, meaningful table."""
    print(f"Info on {len(books)} Books Needed:")
    print("{:<30}{:>8}".format("Book", "Price"))
    for book in books.items():
        print(f"{book[0]:<30}${book[1]:>8.2f}")
        # book[0] being the key and book[1] being the value
    print("{:<30}${:>8.2f}".format("Total", total))
    print("{:<30}${:>8.2f}".format("Average", avg))


print("Welcome to the book list summarizinator 4000")
main()
