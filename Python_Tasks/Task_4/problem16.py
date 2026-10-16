# Problem: Nested Lists

# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

# Your accepted solution code here
if __name__ == '__main__':
    s=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s.append([name, score])

    second_lowest = sorted(set(score for name, score in s))[1]

    names = sorted(
        name for name, score in s
        if score == second_lowest
    )

    for name in names:
        print(name)
