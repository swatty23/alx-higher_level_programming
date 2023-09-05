#!/usr/bin/python3

# Loop to iterate through the first digit (0 to 9)
for first_digit in range(10):
    # Loop to iterate through the second digit (0 to 9)
    for second_digit in range(first_digit + 1, 10):
        if first_digit < 9:
            print("{:d}{:d}, ".format(first_digit, second_digit), end="")
        else:
            print("{:d}{:d}".format(first_digit, second_digit))

# Print a newline character at the end
print()
