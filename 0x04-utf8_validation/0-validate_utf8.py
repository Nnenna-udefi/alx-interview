#!/usr/bin/python3
"""script"""


def validUTF8(data):
    num_bytes = 0

    for num in data:
        binary_rep = format(num, '08b')  # Convert to binary representation

        if num_bytes == 0:
            # Check the leading bits of the binary representation to determine
            # the number of bytes to follow for the current character
            # '0' indicates a single-byte character
            if binary_rep.startswith('0'):
                num_bytes = 0

            # '110' indicates a two-byte character.
            elif binary_rep.startswith('110'):
                num_bytes = 1

            # '1110' indicates a three-byte character.
            elif binary_rep.startswith('1110'):
                num_bytes = 2

            # '11110' indicates a four-byte character.
            elif binary_rep.startswith('11110'):
                num_bytes = 3
            else:
                # Other cases are considered invalid UTF-8 encodings.
                return False
        else:
            if not binary_rep.startswith('10'):
                # checks that the current byte's binary representation
                # starts with '10', as required for continuation bytes.
                return False
            num_bytes -= 1

    # if all characters have been properly encoded num_byte returns to 0
    return num_bytes == 0
