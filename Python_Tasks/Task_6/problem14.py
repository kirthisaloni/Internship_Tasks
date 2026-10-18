# Problem: Set .intersection() Operation
# HackerRank:https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

# Your accepted solution code here

x = int(input())
a = set(map(int, input().split()))

y = int(input())
b = set(map(int, input().split()))

print(len(a.intersection(b)))
