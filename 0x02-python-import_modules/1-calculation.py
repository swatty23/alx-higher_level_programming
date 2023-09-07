#!/usr/bin/python3

# Define the add function directly in your script
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

# Assign values to a and b
a = 1
b = 2

# Calculate the result using the add function
result = add(a, b)

# Print the result
print("{} + {} = {}".format(a, b, result))
