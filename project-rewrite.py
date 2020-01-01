def min(x, y):
    """
    Returns a smaller number from two numbers given as arguments
    """
    return x if x<y else y

def max(x, y):
    """
    Returns a greater number from two numbers given as arguments
    """
    return x if x>y else y

def len(iterable):
    """
    Returns a number of elements in the given iterable data (e.g. string or list)
    """
    count = 0
    for item in iterable:
        count += 1
    return count

def multiply(x, y):
    pass


def pow(x, y):
    pass


def divmod(x, y):
    pass		


# Implement the multiply(x, y) function for integer numbers as inputs! Do not use the *, /, and // operators and any built-in functions, but you may (and should) use +.

#     For any two integer inputs the returned value equals the result of x * y
#     Neither *, /, // nor any built-in functions are used

# pow() 	

# Implement the pow(x, y) function for real base numbers and positive integer exponents! Do not use the ** operator and any built-in functions! Here you can use *.

#     For inputs from the specified domain the returned value equals the result of x**y
#     Neither ** nor any built-in functions are used

# divmod() 	

# OPTIONAL

# Implement the divmod(x, y) function for for two integer numbers as inputs! Do not use the // and the % operators and any built-in functions! It should return a tuple: the first value should be equal to the value of x // y and the second equal to the value of x % y! Do not use the // operator and any built-in functions!

#     For any two positive integer inputs the returned value equals (x // y, x % y)
#     For any two +/- integer inputs the returned value equals (x // y, x % y)
#     Neither // nor any built-in functions are used

