def my():
  n = int(input())
  board = [list(map(int, input().split())) for _ in range(n)]

  result = []
  l_cross = 0
  r_cross = 0

  for i in range(n):
    tmp = 0
    a = 0
    for j in range(n):
      tmp += board[i][j]
      a += board[j][i]

    result.append(tmp)
    result.append(a)
  
  for i in range(n):
    l_cross += board[i][i]
    r_cross += board[i][n-i-1]
    
  result.append(l_cross)
  result.append(r_cross)

  print(max(result))

def solution():
  n = int(input())
  a = [list(map(int, input().split())) for _ in range(n)]
  largest = -2147000000
  for i in range(n):
    sum1=sum2=0
    for j in range(n):
      sum1 += a[i][j]
      sum2 += a[j[i]]
      if sum1>largest:
        largest=sum1
      if sum2>largest:
        largest=sum2
  sum1=sum2=0
  for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
  if sum1>largest:
        largest=sum1
  if sum2>largest:
    largest=sum2
  print(largest)
  
my()

# 열이 세로 행이 가로
# 아니 문제가 좀 더 정확하게 적혀 있어야 하지 않을까?