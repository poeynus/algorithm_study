def my():
  n = int(input())
  ath = []
  cnt = 0
  largest = 0

  for _ in range(n):
    tall, weight = map(int, input().split())
    ath.append((tall, weight))

  ath.sort(reverse=True)

  for t, w in ath:
    if w > largest:
      largest = w
      cnt += 1
  
  print(cnt)

def solution():
  # 똑같아
  pass

my()

# 첫번째 값 부터 이 사람보다 키와 몸무게 둘 다 큰 사람 있으면 탈락

# 키로 정렬, for문 2번 돌리지 말고 최대값 저장해서 비교 해라
# 이렇게 쉬운 방법이 있다니