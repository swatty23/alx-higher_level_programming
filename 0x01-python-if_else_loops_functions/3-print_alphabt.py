#!/usr/bin/python3

# Loop to print the alphabet excluding 'q' and 'e'
for char_code in range(97, 123):  # ASCII values for 'a' to 'z'
    if chr(char_code) not in ['e', 'q']:
        print(chr(char_code), end='')

# Print a newline character at the end
print()
