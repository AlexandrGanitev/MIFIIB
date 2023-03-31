"""Python Program to Check Leap Year
Leap Year:

A year is called a leap year if it contains an additional day which makes the number of the days in that year is 366. This additional day is added in February which makes it 29 days long.

A leap year occurred once every 4 years.

How to determine if a year is a leap year?

You should follow the following steps to determine whether a year is a leap year or not.

If a year is evenly divisible by 4 means having no remainder then go to next step. If it is not divisible by 4. It is not a leap year. For example: 1997 is not a leap year.
If a year is divisible by 4, but not by 100. For example: 2012, it is a leap year. If a year is divisible by both 4 and 100, go to next step.
If a year is divisible by 100, but not by 400. For example: 1900, then it is not a leap year. If a year is divisible by both, then it is a leap year. So 2000 is a leap year.
Look at the following program to understand the implementation of it:

Example:
"""
# Default function to implement conditions to check leap year
def CheckLeap(Year):
  # Checking if the given year is leap year
  if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    print("Given Year is a leap Year");
  # Else it is not a leap year
  else:
    print ("Given Year is not a leap Year")
# Taking an input year from user
Year = int(input("Enter the number: "))
# Printing result
CheckLeap(Year)

print('*' * 25)
def is_leap_year(x):
    return (x % 400 == 0) or (( x % 4 == 0) and ( x % 100 != 0))

year = int(input("Введите год:"))
print(is_leap_year(year))
