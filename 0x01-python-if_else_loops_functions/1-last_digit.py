#!/usr/bin/python3
import random

# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)

# Calculate the last digit of the number
last_digit = abs(number) % 10

# Determine the condition based on the last digit
if last_digit > 5:
    condition = "and is greater than 5"
elif last_digit == 0:
    condition = "and is 0"
else:
    condition = "and is less than 6 and not 0"

# Print the result
print(f"Last digit of {number} is {last_digit} {condition}")
