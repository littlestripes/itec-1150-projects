"""
Program Name: loop-2.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Add up some numbers with a loop.
Dates: 2022-09-23 - File created.
"""

welcome_msg = """
                        |  _)
  __|  _ \\  |   | __ \\  __| | __ \\   _` |
 (    (   | |   | |   | |   | |   | (   |
\\___|\\___/ \\__,_|_|  _|\\__|_|_|  _|\\__, |
                                   |___/

 __ \\   __| _ \\   _` |  __| _` | __ `__ \\
 |   | |   (   | (   | |   (   | |   |   |
 .__/ _|  \\___/ \\__, |_|  \\__,_|_|  _|  _|
_|              |___/
"""

# Welcome the user
print("Welcome to the\n", welcome_msg)
print("it also adds up the digits you count! :^)")

# Get lower bound
print("Please enter a small number, 0 or higher: ", end="")
while True:
    first_num = input()
    if first_num.isnumeric() is False:
        print("c'mon man, give me a NUMBER! i need WHOLE! DIGITS! ", end="")
    elif int(first_num) <= 0:
        print("0 or higher, pal: ", end="")
    else:
        first_num = int(first_num)
        break

# Get upper bound
print("Now give me a larger number that I can count up to: ", end="")
while True:
    second_num = input()
    if second_num.isnumeric() is False:
        print("c'mon man, give me a NUMBER! use DIGITS! ", end="")
    elif int(second_num) <= first_num:
        print("I said larger, funny man: ", end="")
    else:
        second_num = int(second_num)
        break

# Counting loop
total = 0
for i in range(first_num, second_num+1):
    print(i)
    total += i

print(f"The total of all those numbers is {total}.")
