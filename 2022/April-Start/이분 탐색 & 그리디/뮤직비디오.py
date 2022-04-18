def my():
  n, m = map(int, input().split())
  song = list(map(int, input().split()))

  lt = 1
  rt = sum(song)

  while lt <= rt:
    mid = (lt + rt) // 2
    score = 0
    test = []
    di = True

    for i in song:
      if score + i >= mid:
        test.append(score)
        score = 0
      score += i

    if len(test) > m:
      lt = mid + 1
      di = True
    elif len(test) < m:
      rt = mid - 1
      di = False
    elif len(test) == m and di:
      lt = mid + 1
    elif len(test) == m and di == False:
      rt = mid + 1
  print(mid - 1)

def solution():
  n, m = map(int, input().split())
  Music = list(map(int, input().split()))

  lt = 1
  rt = sum(Music)
  maxx=max(Music)
  res = 0
  while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid, Music)<=m:
      res=mid
      rt=mid-1
    else:
      lt=mid+1
  print(res)

def Count(capacity, Music):
  cnt=1
  sum=0
  for x in Music:
    if sum+x>capacity:
      cnt+=1
      sum=x
    else:
      sum+=x
  return cnt

my()

# 이거도 이분 검색
# 가장 큰 값을 기준으로 하나씩 비교하면 될 거 같은데?
# 범위는 가장 큰 값 ~ 전부 더한 값
# 중간 값으로 분기 score
# len이 m 보다 크면 lt = mid + 1, 작으면 rt = mid - 1
# 똑같이 반복 근데 1번문제 자체가 이상한데?