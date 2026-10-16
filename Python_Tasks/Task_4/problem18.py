# Problem: Lists

# HackerRank: https://www.hackerrank.com/challenges/python-lists/problem

# Your accepted solution code here
if __name__ == '__main__':
    N = int(input())
    items=[]
    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            items.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(items)
        elif command[0] == "remove":
            items.remove(int(command[1]))
        elif command[0] == "append":
            items.append(int(command[1]))
        elif command[0] == "sort":
            items.sort()
        elif command[0] == "pop":
            items.pop()
        elif command[0] == "reverse":
            items.reverse()
