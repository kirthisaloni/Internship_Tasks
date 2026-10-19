# Problem: Weighted Uniform Strings

# HackerRank:  https://www.hackerrank.com/challenges/weighted-uniform-string/problem

# Your accepted solution code here
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    weights = set()
    prev = ''
    count = 0
    for ch in s:
        weight = ord(ch) - ord('a') + 1

        if ch == prev:
            count += weight
        else:
            count = weight

        weights.add(count)
        prev = ch

    return ["Yes" if q in weights else "No" for q in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
