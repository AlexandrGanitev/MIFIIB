def spam(number1, number2) :
    return number1 / (number2 - 42)


spam(101, 42)

# The Traceback points to line 5 and then to line 2, where the actual
# ZeroDivision happens. Avoid creating vague situations of this kind.
# Using variable in the /(a - b) contructions needs to be thought over in
# advance!