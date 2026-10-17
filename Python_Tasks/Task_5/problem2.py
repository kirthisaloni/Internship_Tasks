# Problem: String Split and Join

# HackerRank: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

# Your accepted solution code here
def split_and_join(line):
    x=line.split()
    return '-'.join(x)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
