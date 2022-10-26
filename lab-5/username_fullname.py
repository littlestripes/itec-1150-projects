"""
Program Name: username_fullname.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Manages a database of users.
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
\tview -> view the full name of a user
\tadd  -> add a user
\tdel  -> delete a user
\thelp -> display this message
\texit -> exits the program
"""


def main():
    # initialize users dict
    users = {
        "xXxbubbafrumpstreestumpxXx": "Bobby Hill",
        "mrbillohno": "Connor Chuckles",
        "jimvarney66": "Ernest Worrell"
    }
    print("Welcome to the user database.")
    display_menu()  # tell the user what their options are

    # main program loop
    while True:
        command = get_command()
        # then parse the command
        if command == "view":
            view(users)
            pass
        elif command == "add":
            add(users)
            pass
        elif command == "del":
            delete(users)
            pass
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


def view(users: dict):
    """
    Asks the user which username to look up and prints the full name associated
    with it, if there is one.

    :param users: dict of format `username: full_name`
    """
    display_usernames(users)
    username = str(input("Enter user to view: "))
    if username in users:
        full_name = users[username]
        print(f"{username}'s full name is {full_name}.")
    else:
        print(f"There is no user with the username {username}.")
        print("Would you like to add one? (y or n)")
        while True:
            command = str(input("> "))
            if command == "y":
                add(users, from_view=True)
                return
            elif command == "n":
                print("Returning to main menu...")
                return
            else:
                print("Come now, I'm a busy computer. I need an answer.")


def add(users: dict, from_view: bool = False):
    """
    Adds a user to the users dict.

    :param users: reference to dict of format `username: full_name`
    :param from_view: whether or not calling function was view()
    """
    if not from_view:
        # if view() called this function, we don't display the usernames a
        # second time
        display_usernames(users)

    username = str(input("Enter username of new user: "))
    if username in users:
        print(f"{username} already exists.")
        # add ability to update existing user's name
    else:
        full_name = str(input("Enter user's full name: "))
        full_name = full_name.title()
        users[username] = full_name
        print(f"{full_name} was added.")


def delete(users: dict):
    """
    Deletes a specified user from the referenced dict of users.

    :param users: reference to dict of format `username: full_name`
    """
    display_usernames(users)
    username = str(input("Enter username of user to delete: "))
    if username in users:
        full_name = users.pop(username)
        print(f"{full_name} was deleted from the database.")
    else:
        print(f"{username} does not exist.")


def display_usernames(users: dict):
    """
    Prints a list of usernames from the dict provided.

    :param users: dict of format `username: full_name`
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
