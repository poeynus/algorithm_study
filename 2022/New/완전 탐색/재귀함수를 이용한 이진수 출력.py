def my():
  n = int(input())
  recursive(n)

def recursive(x):
  if x == 0:
    return
  else:
    recursive(x//2)
    print(x % 2, end='')

def solution():
  n=int(input())
  DFS(n)

def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')

my()

# 5  0
# 2  1
# 1  0

# 계속 2로 나누고 나머지를 나중에 출력하기

# 되긴 하는데 뒤에 %는 왜 붙는거임? 재귀 부분에서 붙는데