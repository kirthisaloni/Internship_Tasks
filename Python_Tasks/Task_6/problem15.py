# Problem: Set .difference() Operation

# HackerRank:https://www.hackerrank.com/challenges/py-set-difference-operation/problem

# Your accepted solution code here
x = int(input())
a = set(map(int, input().split()))

y = int(input())
b = set(map(int, input().split()))

print(len(a.difference(b)))
