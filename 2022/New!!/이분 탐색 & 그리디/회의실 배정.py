def my():
  pass

def solution():
  n = int(int())
  meeting = []
  for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))
  meeting.sort(key=lambda x : (x[1], x[0])) # 이거는 순위를 바꿔서 정렬한다는 뜻
  
  et = 0
  cnt = 0

  for s, e in meeting:
    if s >= et:
      et = e
      cnt += 1
  print(cnt)

my()

# 끝나는 시간 순으로 정렬, 가장 빨리 끝나는 회의를 먼저 시작
# 끝나는 시간과 다음 회의 시작 시간이 같거나 커야 한다.