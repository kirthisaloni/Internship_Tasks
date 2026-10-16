# Problem: Set .add()

# HackerRank: http://hackerrank.com/challenges/py-set-add/problem

# Your accepted solution code here
n = int(input())
countries = set()

for _ in range(n):
    countries.add(input().strip())

print(len(countries))
