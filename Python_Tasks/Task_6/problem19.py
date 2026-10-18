# Problem: Company Logo
# HackerRank:https://www.hackerrank.com/challenges/most-commons/problem

# Your accepted solution code here
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input()

    count = Counter(s)

    result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    for char, freq in result[:3]:
        print(char, freq)
