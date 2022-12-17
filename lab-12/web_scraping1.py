"""
Program Name: web_scraping1.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Downloads a .txt file, opens it, reads it, and prints it to standard output.
Dates: 2022-12-16 - File created.
"""

import requests  # get


def main():
    # very simple task, we make the request first:
    req = requests.get("https://gutenberg.org/cache/epub/32540/pg32540.txt")
    print("Sending request to server...")
    # check for errors
    try:
        req.raise_for_status()
    except Exception as error:
        print(f"Uh oh! {error}")
        return

    # download file to local .txt
    print("Writing to file...")
    with open("muir.txt", "wb") as file:
        for chunk in req.iter_content(100000):
            file.write(chunk)

    # then read it
    with open("muir.txt") as file:
        # and print it
        print("Reading from file...")
        for line in file.readlines():
            print(line, end="")  # file already contains newlines


if __name__ == "__main__":
    main()
