# Problem: The Minion Game

# HackerRank:https://www.hackerrank.com/challenges/the-minion-game/problem

# Your accepted solution code here
def minion_game(string):
    v="AEIOU"
    s=0
    k=0
    n=len(string)
    
    for i in range(n):
        if string[i] in v:
            k+=n-i
        else:
            s+=n-i
    if k>s:
        print('Kevin',k)
    elif s>k:
        print('Stuart',s)
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
