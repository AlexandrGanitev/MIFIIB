def check_var_type(some_var):
    if some_var is None :
        print("NoneType")
    else :
        if type(some_var) == tuple:
            print("This is a tuple type -", some_var)
        elif type(some_var) == list:
            print("This is a list type -", some_var)
        # print(type(some_var))


check_var_type(None)
check_var_type((2,))
check_var_type([1, 5, 3])
