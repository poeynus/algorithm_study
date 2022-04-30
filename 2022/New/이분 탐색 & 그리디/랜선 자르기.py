from itertools import count


def my():
  n, m = map(int, input().split())
  lan_list = [int(input()) for _ in range(n)]

  lt = 1
  rt = max(lan_list)
  mid = 0

  while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0
    di = True

    for i in lan_list:
      cnt += (i // mid)

    if cnt > m:
      lt = mid + 1
      di = True
    elif cnt < m:
      rt = mid - 1
      di = False
    elif cnt == m and di:
      lt = mid + 1
    elif cnt == m and di == False:
      rt = mid - 1 

  print(mid - 1)

def solution():
  k, n = map(int, input().split())
  Line = []
  res = 0
  largest=0
  for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest = max(Line)
  lt=1
  rt=largest
  while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid, Line)>=n:
      res=mid
      lt=mid+1
    else:
      rt=mid-1
  print(res)
  
def Count(len, Line):
  cnt=0
  for x in Line:
    cnt += (x//len)
my()

# 결정 알고리즘 사용 - 아직 검색 해보진 않았는데 이분 검색 응용 문제인 듯
# 어차피 랜선 길이가 가장 큰 값을 넘어서는 길이로 자를 수는 없으니 lt, rt의 초기 값을 lt = 1, rt = 가장큰 값으로 잡는다.
# mid 위치 구한 뒤 입력 받은 랜선들을 전부 mid 값으로 나눠 보고 비교
# 나눠지는 랜선이 더 많으면 lt = mid + 1, 적으면 rt = mid - 1, 같을 경우는?
# 값이 lt > rt가 될때 까지 반복

# 깨달아 버렸다.