# Problem: Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/symmetric-difference/problem

# Your accepted solution code here
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
for value in sorted(a ^ b):
    print(value)
