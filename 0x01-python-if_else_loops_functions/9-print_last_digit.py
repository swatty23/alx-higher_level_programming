#!/usr/bin/python3

def print_last_digit(number):
    # Calculate the last digit using the absolute value of the number
    last_digit = abs(number) % 10

    # Print the last digit
    print(last_digit, end="")

    # Return the value of the last digit
    return last_digit
