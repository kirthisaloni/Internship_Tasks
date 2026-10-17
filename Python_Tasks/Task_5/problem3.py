# Problem: Mutations

# HackerRank: https://www.hackerrank.com/challenges/python-mutations/problem

# Your accepted solution code here
def mutate_string(string, position, character):
    s = string[:position] + character + string[position+1:]
    return s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
