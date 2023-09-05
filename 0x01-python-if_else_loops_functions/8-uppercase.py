#!/usr/bin/python3

def uppercase(s):
    # Initialize an empty string for the uppercase result
    result = ""

    # Loop through each character in the input string
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII values
            result += chr(ord(char) - 32)
        else:
            # Keep non-lowercase characters unchanged
            result += char

    # Print the resulting uppercase string followed by a newline
    print(result)
