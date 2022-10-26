"""
Program Name: wage_calc.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    This script calculates gross pay based on regular and overtime rates.
Dates: 2022-08-30 - File created.
"""

# Initialize variables
regular_hours_worked = 40
overtime_hours_worked = 10
regular_wage = 15.34

# Calculate total pay
overtime_wage = regular_wage * 1.5
gross_pay = (regular_hours_worked * regular_wage) + (overtime_hours_worked * overtime_wage)

# Print result to user
print(f"Your gross pay is ${gross_pay:.2f}.")
