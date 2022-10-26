""" M. Bock 6/13/2019 This counting program allows the user to determine
a start and stop number for our range function. It displays each number
counted, adds each digit to the next & displays the results """

# greet the user
print('Welcome to our counting program.')
print('It also adds up the digits that you count!')

# collect user's start number for the counting game
start_num = input('Please enter a small number, 0 or higher: ')
while start_num.isnumeric() is False:  # validate the input
    start_num = input('Enter a whole number: ')
start_num = int(start_num)  # when validated, convert to int

# collect user's stop number for the counting game
stop_num = input('Now, enter a larger number that you want to count up to: ')
while stop_num.isnumeric() is False or int(stop_num) <= start_num:  # validate 2 ways
    stop_num = input(f'Enter a whole number greater than your start number ({start_num}): ')
stop_num = int(stop_num)  # when validated, convert to int

# run counting program, based on user start and stop number
total = 0  # initialize an accumulator
for number in range(start_num, stop_num +1):
    print(number)
    total += number # shorthand for total = total + number

# display the total accumulated in a sentence
print(f'The total of all the numbers you counted is: {total:,d}.')