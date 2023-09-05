#!/usr/bin/python3

# Loop to print numbers from 0 to 98 in both decimal and hexadecimal
for number in range(99):
    print("{:d} = 0x{:x}".format(number, number))
