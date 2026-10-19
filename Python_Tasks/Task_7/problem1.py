# Problem:Set .symmetric_difference() Operation

# HackerRank:https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

# Your accepted solution code here
a=int(input())
x=set(map(int,input().split()))
b=int(input())
y=set(map(int,input().split()))
print(len(x.symmetric_difference(y)))
