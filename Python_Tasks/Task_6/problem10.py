# Problem: Designer Door Mat

# HackerRank:https://www.hackerrank.com/challenges/designer-door-mat/problem

# Your accepted solution code here
x, y = map(int, input().split())

for i in range(1, x, 2):
    print((".|." * i).center(y, "-"))

print("WELCOME".center(y, "-"))

for i in range(x - 2, 0, -2):
    print((".|." * i).center(y, "-"))
