"""
Program Name: grade.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Displays the equivalent letter grade for a user-provided quiz score.
Dates: 2022-09-17 - File created.
"""

# Accept quiz score and store in variable
score = input("Enter quiz score -- whole number 0-100: ")

# Validate input
if score.isnumeric() is False:
    print("Try the program again; it only takes whole numbers.")
else:
    score = int(score)
    # Tell the user all about that little letter grade of theirs
    if score >= 90:
        print("You got an A. Good job!")
    elif score >= 80:
        print("You got a B. B for Better luck next time!")
    elif score >= 70:
        print("You got a C. Aggressively mediocre, if I do say so myself.")
    elif score >= 60:
        print("You got a D. Not only did you not pass, but you also failed.")
    else:
        print("You got an F. Fire up that Xbox, my friend; you're a bona fide burnout!")
