# create an input to ask the user for a string representing a number ex: 34fc
# ask the user to input a base power ex: 2-16
# then compute the string into an integer in decimal and in binary with the
# corresponding base power for decimal and binary

number_string = input("Enter a number using 0-9 and/or A-F: ")
base_number = int(input("What is the base power? Enter a number between 2-16: "))

# convert the string into the decimal number and then binary number

decimal_number = int(number_string, base_number)
binary_number = bin(int(number_string, base_number))[2:]

# once input is converted to decimal and binary display the input values and results
print(number_string,'in base ', base_number,': is ', decimal_number,'in base 10 and ', binary_number, 'in base 2')

