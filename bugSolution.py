def my_function(x):
    try:
        if isinstance(x, (int, float)):
            if x == 0:
                return 0
            else:
                return 1 / x
        else:
            raise TypeError("Input must be a number.")
    except ZeroDivisionError:
        return "Division by zero!"
    except TypeError as e:
        return f"Error: {e}"