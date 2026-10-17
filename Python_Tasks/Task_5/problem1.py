# Problem: Find the Runner-Up Score!
# HackerRank:https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# Your accepted solution code here
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=sorted(set(arr))
    print(a[-2])
