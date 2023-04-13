def a() :
    print('Start of a()')
    b()  # Call b().


def b() :
    print('Start of b()')
    c()  # Call c().


def c() :
    print('Start of c()')
    42 / 0  # This will call a ZeroDivision error.


a()  # Calling a().
#
# The error is thrown in the line, where the functions starts,
# which means you need to investigate the lines after or sometimes above.
#
