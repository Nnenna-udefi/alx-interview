#!/usr/bin/python3
"""
    script that reads stdin line by line and computes metrics
"""
import sys

# initialize variables to store metrics
total_file_size = 0
code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
processed_line = 0


if __name__ == '__main__':
    try:
        for line in sys.stdin:
            try:
                data = line.split()
                ip_address = data[0]
                status_code = int(data[-2])
                file_size = int(data[-1])

                total_file_size += file_size
                if status_code in code:
                    code[status_code] += 1

                processed_line += 1

                # After every 10 lines print statistics
                if processed_line % 10 == 0:
                    print("File size: {}".format(total_file_size))
                    for cod, count in sorted(code.items()):
                        if count:
                            print("{}: {}".format(cod, count))
            except(IndexError, ValueError):
                # if the input format is not correct, skip the lines
                pass
    except KeyboardInterrupt:
        # if the keyboard is interrupted (control C) print final statistics
        print("File size: {}".format(total_file_size))
        for cod, count in sorted(code.items()):
            if count > 0:
                print("{}: {}".format(cod, count))
        raise
