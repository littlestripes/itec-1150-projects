"""
Program Name: directory_file.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Manages a database of users stored in a text file.
Dates: 2022-10-13 - File created.
       2022-12-15 - Adapted from username_fullname.py.
"""

import sys      # exit()
import pathlib  # Path()

VALID_COMMANDS = ["view", "add", "exit", "help"]  # for get_command()
SAMPLE_ENTRY = "unrealmast3r bobbyfischer@princeton.edu.tz\n"
HELP_TEXT = """
=============================================
 ****     **** ******** ****     ** **     **
/**/**   **/**/**///// /**/**   /**/**    /**
/**//** ** /**/**      /**//**  /**/**    /**
/** //***  /**/******* /** //** /**/**    /**
/**  //*   /**/**////  /**  //**/**/**    /**
/**   /    /**/**      /**   //****/**    /**
/**        /**/********/**    //***//*******
//         // //////// //      ///  ///////   2!
=============================================
\tview -> view the email of a user
\tadd  -> add a user
\thelp -> display this message
\texit -> exits the program
"""


def main():
    # check if database file exists; if not, make one with the sample entry
    db_path = pathlib.Path('./db.txt')
    if not db_path.exists():
        with db_path.open(mode="w") as db:
            db.writelines(SAMPLE_ENTRY)

    # from the db file, read the usernames and emails and store them in a dict
    db_dict = dict()
    with db_path.open() as db:
        entries = db.readlines()  # get a list of the entries as strings first
        for item in entries:
            username, email = item.split()
            db_dict.update({username: email})

    print("Welcome to the email database terminal.")
    display_menu()  # tell the user what their options are

    # main program loop
    while True:
        command = get_command()
        # then parse the command
        if command == "view":
            view(db_dict, db_path)  # if view() calls add(), it needs db_path
        elif command == "add":
            add(db_dict, db_path)
        elif command == "help":
            display_menu()
        elif command == "exit":
            print("Your users thank you for your deft HR skills.")
            sys.exit()
        else:
            print("You shouldn't have done that.")
            detonate()


def display_menu():
    """Prints the menu to screen."""
    print(HELP_TEXT)


def view(users: dict, db_path: pathlib.Path):
    """
    Asks the user which username to look up and prints the email associated
    with it, if there is one.

    :param users: dict of format `username: email`
    :param db_path: Path object, path of database file (default is "./db.txt")
    """
    display_usernames(users)
    username = str(input("Enter user to view: "))
    if username in users:
        email = users[username]
        print(f"{username}'s email address is {email}.")
    else:
        print(f"There is no user with the username {username}.")
        print("Would you like to add one? (y or n)")
        while True:
            command = str(input("> "))
            if command == "y":
                add(users, db_path, from_view=True, _username=username)
                return
            elif command == "n":
                print("Returning to main menu...")
                return
            else:
                print("Come now, I'm a busy computer. I need an answer.")


def add(users: dict, db_path: pathlib.Path, from_view: bool = False, _username: str = None):
    """
    Adds a user to the users dict.

    :param users: reference to dict of format `username: email`
    :param db_path: Path object, path of database file (default is `./db.txt`)
    :param from_view: whether or not calling function was view()
    :param username: str, username to be added, can be passed in
        to bypass prompt
    """
    if not from_view:
        # if view() called this function, we don't display the usernames a
        # second time
        display_usernames(users)

    new_entries_dict = dict()
    # note: the only way that a single entry can be added at one time is if
    # this function is called by view, in which case it'll have one passed in
    if _username:
        email = str(input(f"Enter {_username}'s email address: "))
        new_entries_dict.update({_username: email})
    else:
        print("Please enter username/email combinations in this format:")
        print("\tusername email, username email, ...")
        _input = str(input("# "))
        new_entries = _input.split(",")  # make a list
        new_entries = [entry.strip() for entry in new_entries]  # clean 'em up
        for entry in new_entries:
            try:
                username, email = entry.split()
            except ValueError:  # if user doesn't follow the format, typically
                print("Error! You did it wrong! Punk!")
                print("Returning to main menu...")
                return
            if not users.get(username):  # check one more time
                new_entries_dict.update({username: email})

    # add to the users dict, then to the db file
    users.update(new_entries_dict)
    with db_path.open("a") as db:
        for username, email in new_entries_dict.items():
            db.writelines(f"{username} {email}\n")
    print("New users were added successfully.")


def display_usernames(users: dict):
    """
    Prints a list of usernames from the dict provided.

    :param users: dict of format `username: email`
    """
    usernames = list(users.keys())
    # then typecast as str joined by ,
    usernames = ", ".join(usernames)
    print(f"Users: {usernames}\n")


def get_command() -> str:
    """
    Accepts input command from user and validates it, returning it if valid.

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
