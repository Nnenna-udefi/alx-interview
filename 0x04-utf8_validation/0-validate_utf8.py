#!/usr/bin/python3
"""script"""


def validUTF8(data):
    num_bytes_to_follow = 0

    for num in data:
        binary_rep = format(num, '08b')  # Convert to binary representation

        if num_bytes_to_follow == 0:
            if binary_rep.startswith('0'):
                num_bytes_to_follow = 0
            elif binary_rep.startswith('110'):
                num_bytes_to_follow = 1
            elif binary_rep.startswith('1110'):
                num_bytes_to_follow = 2
            elif binary_rep.startswith('11110'):
                num_bytes_to_follow = 3
            else:
                return False
        else:
            if not binary_rep.startswith('10'):
                return False
            num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0
