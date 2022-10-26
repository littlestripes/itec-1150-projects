"""
Program Name: book_list.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Tabulate the costs of a series of books.
Dates: 2022-10-05 - File created.
"""

import sys  # exit()


def main():
    books = inputs()  # populate a dict with book names and prices
    total, average = processing(books.values())  # use said prices to get mean and total
    outputs(books, total, average)  # format for user-friendly use

    # restart loop
    while True:
        restart = str(input("Need more books? (y or n): "))
        if restart == "y":
            main()
        elif restart == "n":
            print("Thanks for your time.")
            sys.exit()
        else:
            print("Some huh?")


def inputs() -> dict:
    """Returns a dict of book names and prices."""
    num_books = get_pos_int()

    books = dict()
    # populate the empty dict with book details
    for book in range(1, num_books+1):
        book_name = str(input(f"Name of book {book}: "))
        book_price = get_pos_int("Please enter the cost of the book to the nearest dollar: ")
        books[book_name] = book_price

    return books


def get_pos_int(prompt="Please enter a whole number: ") -> int:  # collect and validate an int > 0
    pos_int = input(prompt)
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int


def processing(book_prices: list):
    """Returns total and mean prices for the price list supplied."""
    book_price_avg = sum(book_prices) / len(book_prices)
    return sum(book_prices), round(book_price_avg, 2)


def outputs(books: dict, total: int, avg: float):
    """Outputs the data in a beautiful, meaningful table."""
    print(f"Info on {len(books)} Books Needed:")
    print("{:<30}{:>8}".format("Book", "Price"))
    for book in books.items():
        print(f"{book[0]:<30}${book[1]:>8.2f}")  # book[0] being the key and book[1] being the value
    print("{:<30}${:>8.2f}".format("Total", total))
    print("{:<30}${:>8.2f}".format("Average", avg))


print("Welcome to the book list summarizinator 4000")
main()
