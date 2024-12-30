def my_function(x):
    if x == 0:
        return 0  # This line causes an error if x is a list or other non-numeric type
    else:
        return 1 / x