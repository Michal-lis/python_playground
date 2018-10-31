#!/usr/bin/env python3
import sys

for arg in sys.argv[1:]:
    i = 0
    try:
        with open(arg, 'r') as infile:
            for line in infile:
                i += 1
    except FileNotFoundError:
        print(arg, "Please make sure this file exists!")
    else:
        print(arg, "numer of lines: " + str(i))

# "python3 CountLines file1.txt file2.txt file3.txt"
