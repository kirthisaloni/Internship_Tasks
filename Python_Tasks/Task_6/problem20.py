# Problem: Validating phone numbers
# HackerRank:https://www.hackerrank.com/challenges/validating-the-phone-number/problem?

# Your accepted solution code here
import re

n = int(input())

for _ in range(n):
    s = input()
    
    if re.match(r'^[789]\d{9}$', s):
        print("YES")
    else:
        print("NO")
