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
    """
    Returns a result of multiplying two integers without using /, // and * or any built-in functions
    """
    result = 0
    for number in range(0, x):
        result += y
    return result


def pow(x, y):
    """
    Returns a result of exponantiating two integers without using ** or any built-in functions
    """
    result = 1
    for number in range(0, x):
        result *= y
    return result


def divmod(x, y):
    """
    For two integer numbers as inputs, returns the tuple with first value as a result of x // y 
    and the second as a result of x % y without using // or % operators or any built-in functions.
    """ 	
    floor_division_result = 0
    
    if x*y > 0 and x > 0:
        while (floor_division_result + 1) * y <= x:
            floor_division_result += 1
    elif x*y > 0 and x < 0:
        while (floor_division_result + 1) * -y <= -x:
            floor_division_result += 1
    elif x*y < 0 and x > 0:
        while (floor_division_result) * y < x:
            floor_division_result -= 1
    elif x*y < 0 and x < 0:
        while (floor_division_result) * y > x:
            floor_division_result -= 1

    modulo_result = x - (y * floor_division_result)
    
    if y != 0:
        return (floor_division_result, modulo_result)
    else:
        return "You can't divide by 0"



print(divmod(2, 8))
print(2 // 8)
print(2 % 8)



# dodać min i max ale dla list	

# OPTIONAL


# How can you divide and calulate modulo without actually dividing? 
# Try to add up numbers until you reach the goal! 
# We'll test only with not too large numbers (between -100 and 100). 
# Also, reproducing integer division can be tricky; as you can read in the documentation, 
# "The result is always rounded towards minus infinity: 1//2 is 0, (-1)//2 is -1, 1//(-2) is -1, and (-1)//(-2) is 0."