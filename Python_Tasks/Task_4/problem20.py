# Problem: No Idea!

# HackerRank: https://www.hackerrank.com/challenges/no-idea/problem

# Your accepted solution code here
n, m = map(int, input().split())
a = list(map(int, input().split()))
l = set(map(int, input().split()))
d = set(map(int, input().split()))

happiness = sum((value in l) - (value in d) for value in a)
print(happiness)
