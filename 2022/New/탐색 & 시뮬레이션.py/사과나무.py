def my():
  n = int(input())
  apple = [list(map(int, input().split())) for _ in range(n)]
  a = b = n // 2
  result = 0

  for i in range(n):   # 0 1 2
    for j in range(a, b+1): # 1 2
      result += apple[i][j]

    if i >= n // 2:
      a += 1
      b -= 1
    else:
      a -= 1
      b += 1
  print(result)

def solution():
  n = int(input())
  a = [list(map(int, input().split())) for _ in range(n)]
  res=0
  s=e=n//2
  for i in range(n):
    for j in range(s, e+1):
      res+=a[i][j]
    if i<n//2:
      s-=1
      e+=1
    else:
      s+=1
      e-=1
  print(res)

my()

# n 입력 그 후 n*n 배열 입력
# 그냥 3개로 꽂아 a, b, c
# 처음에는 가운데서 시작
# 그 후 위치만 변동 b는 고정 a = b - 1, c = b + 1
# 그럼 범위 값을 다 더하면 됨
# 그 후 a 부터 b의 거리가 n이랑 같으면 다시 하나씩 감소
# 이거 반복
# 알 깼다. 강사님이랑 풀이도 똑같음