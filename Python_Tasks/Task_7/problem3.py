# Problem:Mars Exploration

# HackerRank:  https://www.hackerrank.com/challenges/mars-exploration/problem

# Your accepted solution code here
#!/bin/python3

import math
import os
import random
import re
import sys

def marsExploration(s):
    # Write your code here
    x='SOS'
    c=0
    for i in range(len(s)): 
        if s[i] != x[i % 3]:
            c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
