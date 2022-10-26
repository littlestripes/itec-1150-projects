"""
Program Name: author_book.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Manages a database of one's favorite books.
Dates: 2022-10-13 - File created.
"""

import sys  # exit()

VALID_COMMANDS = ["view", "add", "del", "exit", "help"]  # for get_command()
HELP_TEXT = """
=============================================
 ****     **** ******** ****     ** **     **
/**/**   **/**/**///// /**/**   /**/**    /**
/**//** ** /**/**      /**//**  /**/**    /**
/** //***  /**/******* /** //** /**/**    /**
/**  //*   /**/**////  /**  //**/**/**    /**
/**   /    /**/**      /**   //****/**    /**
/**        /**/********/**    //***//*******
//         // //////// //      ///  ///////
=============================================
\tview -> view the book(s) by an author
\tadd  -> add an author
\tdel  -> delete an author
\thelp -> display this message
\texit -> exits the program
"""


def main():
    # initialize readings dict
    readings = {
        "Kirk Van Houten": "Can I Borrow A Feeling?",
        "Lucifer": "Necronomicon",
        "Edgar Allan Poe": "Could You Be Loved? The Bob Marley Story"
    }
    print("Welcome to the reading database.")
    display_menu()  # tell the user what their options are

    # main program loop
    while True:
        command = get_command()
        # then parse the command
        if command == "view":
            view(readings)
            pass
        elif command == "add":
            add(readings)
            pass
        elif command == "del":
            delete(readings)
            pass
        elif command == "help":
            display_menu()
        elif command == "exit":
            print("Reading rainbow!")
            sys.exit()
        else:
            print("You shouldn't have done that.")
            detonate()


def display_menu():
    """Prints the menu to screen."""
    print(HELP_TEXT)


def view(readings: dict):
    """
    Asks the user which author to look up and prints the book associated
    with them, if there is one.

    :param readings: dict of format `author: book`
    """
    display_authors(readings)
    author = str(input("Enter reading to view: "))
    if author in readings:
        book = readings[author]
        print(f"{author} wrote {book}.")
    else:
        print(f"There is no reading with the author {author}.")
        print("Would you like to add one? (y or n)")
        while True:
            command = str(input("> "))
            if command == "y":
                add(readings, from_view=True)
                return
            elif command == "n":
                print("Returning to main menu...")
                return
            else:
                print("Come now, I'm a busy computer. I need an answer.")


def add(readings: dict, from_view: bool = False):
    """
    Adds a reading to the readings dict.

    :param readings: reference to dict of format `author: book`
    :param from_view: whether or not calling function was view()
    """
    if not from_view:
        # if view() called this function, we don't display the authors a
        # second time
        display_authors(readings)

    author = str(input("Enter author of new book: "))
    if author in readings:
        print(f"{author} already exists in the database.")
        # add handling for multiple books by same author? (list as value?)
    else:
        book = str(input("Enter book's title: "))
        book = book.title()
        readings[author] = book
        print(f"{book} was added.")


def delete(readings: dict):
    """
    Deletes a specified author from the referenced dict of readings.

    :param readings: reference to dict of format `author: book`
    """
    display_authors(readings)
    author = str(input("Enter author to delete: "))
    if author in readings:
        book = readings.pop(author)
        print(f"{book} was deleted from the database.")
    else:
        print(f"{author} does not exist.")


def display_authors(readings: dict):
    """
    Prints a list of authors from the dict provided.

    :param readings: dict of format `author: book`
    """
    authors = list(readings.keys())
    # then typecast as str joined by ,
    authors = ", ".join(authors)
    print(f"Authors: {authors}\n")


def get_command() -> str:
    """
    Accepts input command from reading and validates it, returning it if valid.

    :returns: valid command to be parsed by main()
    """
    while True:
        command = str(input("$ "))
        if not command.isalpha() or command not in VALID_COMMANDS:
            print("Invalid command. (hint: enter 'help' for a list of commands.)")
            continue
        else:
            return command.lower()


def detonate():
    # gotcha!
    pass


if __name__ == "__main__":
    main()
