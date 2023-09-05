#!/usr/bin/python3
import random

# Generate a random signed number between -10 and 10
number = random.randint(-10, 10)

# Check if the number is positive, negative, or zero and print the result
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
