# Problem: Set Mutations
# HackerRank:https://www.hackerrank.com/challenges/py-set-mutations/problem

# Your accepted solution code here
n = int(input())
a = set(map(int, input().split()))

k = int(input())

for _ in range(k):
    op, length = input().split()
    b = set(map(int, input().split()))

    if op == "update":
        a.update(b)

    elif op == "intersection_update":
        a.intersection_update(b)

    elif op == "difference_update":
        a.difference_update(b)

    elif op == "symmetric_difference_update":
        a.symmetric_difference_update(b)

print(sum(a))
