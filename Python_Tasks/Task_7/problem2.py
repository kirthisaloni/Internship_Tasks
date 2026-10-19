# Problem: The Captain's Room
# HackerRank:  https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Your accepted solution code here
k=int(input())
l=list(map(int,input().split()))
unique_sum = sum(set(l)) 
total_sum = sum(l) 
captain = (unique_sum * k - total_sum) // (k - 1) 
print(captain)
