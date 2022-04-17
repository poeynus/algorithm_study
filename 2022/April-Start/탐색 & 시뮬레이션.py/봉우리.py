def my():
  n = int(input())
  new_list = [[0] * (n+2)]
  cnt = 0

  for i in range(n):
    tmp = list(map(int, input().split()))
    tmp.insert(0, 0)
    tmp.append(0)
    new_list.append(tmp)
  new_list.append([0] * (n+2))

  for i in range(1, n+1):
    for j in range(1, n+1):
      if(new_list[i][j] > new_list[i-1][j] and new_list[i][j] > new_list[i][j-1] and new_list[i][j] >  new_list[i][j+1] and new_list[i][j] >  new_list[i+1][j]):
        cnt += 1
 
  print(cnt)

def solution():
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  cnt=0
  n = int(input())
  a=[list(map(int,input().split())) for _ in range(n)]
  a.insert(0, [0]*n)
  a.append([0]*n)
  for x in a:
    x.insert(0,0)
    x.append(0)
  for i in range(1,n+1):
    for j in range(1, n+1):
      if all(a[i][j]>a[i+dx[k]][j+dy[k]]for k in range(4)):
        cnt += 1
  print(cnt)
my()

# 입력 받고 주변을 전부 0으로 감싸기
# 처음 부터 비교 하는데 값이 0이면 그냥 pass
# 0이 아니면 상하좌우 값을 비교하고 현재 값이 제일크면 cnt + 1
# 값이 제일 크면 0으로 바꿨었는데 이럼 문제가 생긴다 0으로 바꾼 값이 다음 값보다 클 경우
# 강사님이 푼 것처럼 방향 제시하고 하면 보기 좋은데 까먹었다.