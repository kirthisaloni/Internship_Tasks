# Problem: Tuples

# HackerRank:https://www.hackerrank.com/challenges/python-tuples/problem
# Your accepted solution code here
n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))
