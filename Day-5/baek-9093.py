import sys

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    word_list = list(input().split())
    for i in word_list:
        print(i[::-1], end=" ")
    print()