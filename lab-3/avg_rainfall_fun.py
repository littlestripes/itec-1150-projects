"""
Program Name: avg_rainfall_fun.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Calculates total and average rainfall based on data collected monthly.
Dates: 2022-10-01 - Modified to conform to the MIPO model.
       2022-10-11 - Fixed yearly_rainfall_avg_grand calculation bug as well as
                    a newly discovered bug (monthly rainfall verification loop
                    would continue despite bad input).
"""


def main():
    # Grand (as in overall) input of number of years to ask for monthly
    # rainfall for.
    # mipo inputs(): For mipo style this is one of the inputs.  We are
    # calling it inputs_grand().
    n_years_grand = inputs_grand("How many years are in your rainfall sample? ")

    # Process.  This is a little more complex than what we went over.  We
    # need to process each year's entries separately.  Each year has it's
    # own mipo processsing loop.  We also need to keep track of the running
    # total of rainfall.
    yearly_rainfall_grand_total = 0
    for year in range(1, n_years_grand + 1):
        # This part should ask the 12 questions, "Enter rain for month #1: "
        # 'Enter rain for month #2: ', etc.  Then return the total rain for
        # that year.
        yearly_rainfall_total = inputs_year()

        # process_year(): A straightforward math computation.  Should return
        # the average rainfall for the year.  Returns a number.
        yearly_rainfall_avg = process_year(yearly_rainfall_total)

        # Outputs to the console the answers:
        # 'Total rain in inches for year #1 = <your answer>'
        # 'Year #1 Monthly Avg Rainfall = <your answer>'
        # Note that the year should change as it does in the loop.  Think
        # f-strings...
        output_year(year, yearly_rainfall_total, yearly_rainfall_avg)

        # Keep running tally of yearly rainfall
        yearly_rainfall_grand_total = yearly_rainfall_grand_total + yearly_rainfall_total

    # process (grand).  Process info about all of the years combined.
    # You have already accumulated the yearly_rainfall_grand_total from loop
    # above.  You now need to compute the average rainfall across all years:
    yearly_rainfall_avg_grand = process_grand(n_years_grand, yearly_rainfall_grand_total)

    # output (grand).  Display all of the info for:
    # 'Total rain, all years = <your answer>'
    # 'Average monthly rain, all years = <your answer>'
    output_grand(yearly_rainfall_grand_total, yearly_rainfall_avg_grand)





# ------------------------------------------------------------------------------
# Support functions


def get_pos_int(prompt):
    """
    You need to implement (which should be done already) to get a positive
    integer.  'prompt' is the question that you ask the user.

    :param prompt: String.  What you want to ask the user to get an integer.
    :return: Integer.  A positive integer.
    """
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print("I need an integer, compadre.")
            continue

        if num > 0:
            break
        else:
            print("Gotta be positive, man.")
            continue

    return num


def inputs_grand(prompt):
    """
    'prompt' will hold your question to ask (see the main loop).  You need to
    return an integer that the user enters.

    You *need* to use 'get_pos_int()' function inside of here.

    :param prompt: Question to ask to get number of years to get monthly
                   rainfall for.
    :return: Integer.  Number of years for which to ask for samples.
    """
    return get_pos_int(prompt)


def inputs_year():
    """
    Get the inputs for a given year.  Return the total rainfall for all months
    entered.  You will need to ask the questions here like:
    'Enter rain for month #7: ', etc.

    :return: Float.  A number (possibly decimal).
    """
    total = 0.0
    for month in range(1, 13):
        while True:
            try:
                total += float(input(f"Enter total rainfall for month #{month}: "))
                break
            except ValueError:
                print("Invalid input.")
                continue


    return total


def process_year(yearly_rainfall_total):
    """
    Take the yearly rainfall total and compute the average monthly rainfall.

    :param yearly_rainfall_total:
    :return: Float.  The average rainfall for this year.
    """
    return yearly_rainfall_total / 12.0


def output_year(year, yearly_rainfall_total, yearly_rainfall_avg):
    """
    Prints the info as below to the console:

    'Total rain in inches for year #1 = <your answer>'
    'Year #1 Monthly Avg Rainfall = <your answer>'

    :param year: The year you are dealing with (1, 2, etc.)
    :param yearly_rainfall_total: computed in main loop.
    :param yearly_rainfall_avg: computed in main loop.
    :return: None.  Just prints to console.
    """
    print(f"Total rain in inches for year #{year}: {yearly_rainfall_total:.2f}")
    print(f"Year #{year} Monthly Avg Rainfall = {yearly_rainfall_avg:.2f}")


def process_grand(n_years_grand, yearly_rainfall_grand_total):
    """
    Compute the average monthly rainfall across all of the years entered.

    :param n_years_grand: Total years collected
    :param yearly_rainfall_grand_total: total rainfall across all months collected.
    :return: The average monthly rainfall over all of the years.
    """
    return (yearly_rainfall_grand_total / 12) * n_years_grand


def output_grand(yearly_rainfall_grand_total, yearly_rainfall_avg_grand):
    """
    output (grand).  Display this info:
    'Total rain, all years = <your answer>'
    'Average monthly rain, all years = <your answer>'

    :param yearly_rainfall_grand_total:
    :param yearly_rainfall_avg_grand:
    :return: None.  Just prints to console.
    """
    print(f"Total rain, all years = {yearly_rainfall_grand_total:.2f}")
    print(f"Average monthly rain, all years = {yearly_rainfall_avg_grand:.2f}")


# ------------------------------------------------------------------------------
# Run main
main()
