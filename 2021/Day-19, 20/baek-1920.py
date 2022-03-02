import sys

n = int(input())
n_list = set(sys.stdin.readline().split())
m = int(input())
m_list = list(sys.stdin.readline().split())

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)