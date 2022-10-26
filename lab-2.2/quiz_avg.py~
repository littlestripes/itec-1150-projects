"""
Program Name: quiz_avg.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Averages the scores of each student in a group.
Dates: 2022-09-23 - File created.
"""


def is_positive_int(
    integer,
    error_msg="Gimme a real number, you brutish excuse for a scholar!",
):
    """Validates intness and positivity of integer, returns True or False"""

    negative_msg = "A POSITIVE number, ya silly goose!"

    try:
        int(integer)
    except ValueError:
        print(error_msg)
        return False

    integer = int(integer)

    if integer < 0:
        print(negative_msg)
        return False

    return integer > 0


# Ask how many students there are
while True:
    num_students = input("How many kids ya got? ")
    # Check for intness
    if is_positive_int(num_students):
        num_students = int(num_students)
        break

# Ask how many quizzes there are in similar fashion
while True:
    num_quizzes = input("How many quiz ya got? ")
    if is_positive_int(num_quizzes):
        num_quizzes = int(num_quizzes)
        break

# Score entry loop
for student in range(1, num_students + 1):
    student_total = 0
    print(f"\nQuiz info for student {student}:")
    # Individual quiz score entry loop
    for quiz in range(1, num_quizzes + 1):
        # Ask for score and validate
        while True:
            score = input(f"Gimme a score for quiz {quiz}: ")
            if is_positive_int(
                score, "I thought you'd have gotten the hang of this by now!"
            ):
                break

        student_total += float(score)

    print(f"Total quiz points for student {student}: {student_total:.2f}")
    # Calculate average
    student_average = round(student_total / num_quizzes, 2)
    print("Student {} quiz average = {:.2f}".format(student, student_average))

# Thank the nice user for their time
goodbye = """
 _________________________________
< thank you for using the program >
 ---------------------------------
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
"""

print(goodbye)
