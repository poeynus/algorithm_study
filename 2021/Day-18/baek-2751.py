import sys

n = int(input())
n_list = []

for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

for i in sorted(n_list):
    print(i)