# Problem:Sherlock and the Valid String

# HackerRank:  https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

# Your accepted solution code here
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    from collections import Counter
    freq = Counter(s).values()
    counts = Counter(freq)

    if len(counts) == 1:
        return "YES"

    if len(counts) == 2:
        a, b = counts.keys()
        x, y = counts.values()

        if (a == 1 and x == 1) or (b == 1 and y == 1):
            return "YES"

        if abs(a - b) == 1 and (x == 1 or y == 1):
            return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
