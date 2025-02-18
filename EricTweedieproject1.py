# program that asks the user for their name, age and the current year

#user inputs their name
name = input("What is your name: ")

#user inputs their age
age = eval(input("What is your age: "))

#user inputs the current year
year = eval(input("What year is it?: "))

#calculating year user was born
year1 = (year - age)

year2 = (year - age) + 1

#taking the inputs and outputing the display of;
# Dear name, you were born either in year1 or year2

print("Dear ",name,", you were born either in ",year1,"or",year2)
