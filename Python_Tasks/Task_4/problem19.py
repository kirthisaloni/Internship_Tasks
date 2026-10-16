# Problem: collections.Counter()

# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

# Your accepted solution code here
from collections import Counter

x=int(input())
a=Counter(map(int,input().split()))
n=int(input())

earnings = 0
for i in range(n):
    size, price = map(int, input().split())
    if a[size] > 0:
        earnings += price
        a[size] -= 1

print(earnings)
