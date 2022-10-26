"""
Program Name: coffee_sales.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Tabulate the sales of coffee at a coffee shop using user-provided sales
    data and the price of each type of coffee.
Dates: 2022-09-06 - File created.
"""

# Take input from the user
cups_coffee = int(input("Cups of coffee sold? "))
price_coffee = float(input("Price of a cup of coffee? "))
cups_tea = int(input("Cups of tea sold? "))
price_tea = float(input("Price of a cup of tea? "))
cups_capp = int(input("Cappuccinos sold? "))
price_capp = float(input("Price of a cappuccino? "))

# Calculate sales per drink and total sales
total_coffee = cups_coffee * price_coffee
total_tea = cups_tea * price_tea
total_capp = cups_capp * price_capp

total_cups = cups_coffee + cups_tea + cups_capp
total_sales = total_coffee + total_tea + total_capp

# Display calculations to user
table_header_str = "{0:<14}{1:<12}{2:<10}{3:<12}"
table_row_str = "{0:<14}{1:<12}${2:<10.2f}${3:<12.2f}"
# formatting template for the table's header and rows
print("Drink Sales for the Reporting Period")
print(table_header_str.format("Drink Type", "Cups Sold", "Price per", " Total"))
print(table_row_str.format(
    "Coffee", cups_coffee, price_coffee, total_coffee
))
print(table_row_str.format("Tea", cups_tea, price_tea, total_tea))
print(table_row_str.format("Cappuccino", cups_capp, price_capp, total_capp))
print("{0:<14}{1:<12}{2:<10} ${3:<12.2f}".format(
    "Total", total_cups, "", total_sales
))
