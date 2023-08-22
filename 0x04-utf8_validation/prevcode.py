#!/usr/bin/python3
"""
    method that determines if a given data set represents
    a valid UTF-8 encoding
"""


def validUTF8(data):
    """ data: list"""

    # For each integer in the data array
    for num in data:
        # convert the value num into a binary representation
        # and extract the last 8 characters form the binary string
        binary_rep = format(num, '08b')

        no_bytes = 0  # Number of bytes in the current UTF-8 character

        if binary_rep[0] == '0':
            no_bytes = 1
        elif binary_rep[0] == '1':
            for bit in binary_rep:
                # get the number of 1s in the beginning of the string
                if bit == '0':
                    break
                no_bytes += 1

            # Setting the character to be 1 to 4 bytes long
            if no_bytes == 1 or no_bytes > 4:
                return False
        else:
            return False

        # Continuation Byte Check
        if no_bytes > 1:
            if not (binary_rep[1] == '1' and binary_rep[2] == '0'):
                return False

        # Reduce the number of bytes to process by 1 after each integer.
        no_bytes -= 1

    # Check if data is complete for a particular UTF-8 character
    return no_bytes == 0
