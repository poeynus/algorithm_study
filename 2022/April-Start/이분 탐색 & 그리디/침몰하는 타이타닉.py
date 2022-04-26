def my():
  n, m = map(int, input().split())
  titanic = list(map(int, input().split()))
  titanic.sort()
  cnt = 0

  while titanic:
    if len(titanic) == 1:
      cnt += 1
      titanic.pop()
    elif titanic[0] + titanic[-1] <= m:
      cnt += 1
      titanic.pop()
      titanic.pop(0)
    else:
      titanic.pop()
      cnt += 1
  print(cnt)

def solution():
  # 똑같음
  pass

my()

# 일단 입력값 오름차순 정렬, 가장 작은 값 + 큰 값 이 무게 제한 보다 작으면 pop 아니면 가장 큰 값 pop 자료구조 빌 때 까지