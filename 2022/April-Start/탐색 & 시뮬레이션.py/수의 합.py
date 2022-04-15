def my():
  n, m = map(int, input().split())
  n_list = list(map(int, input().split()))
  cnt = 0

  for i in range(len(n_list)):
    score = 0
    if n_list[i] > m:
      pass
    elif n_list[i] == m:
      cnt += 1
    else:
      score += n_list[i]

      for j in range(i + 1, len(n_list)):
        if n_list[j] + score > m:
          break
        elif n_list[j] + score == m:
          cnt += 1
          break
        else:
          score += n_list[j]
  print(cnt)

def solution():
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  lt = 0
  rt = 1
  tot = a[0]
  cnt = 0
  while True:
    if tot<m:
      if rt<n:
        tot+=a[rt]
        rt+=1
      else:
        break
    elif tot==m:
      cnt+=1
      tot -= a[lt]
      lt+=1
    else:
      tot-=a[lt]
      lt+=1
  print(cnt)

solution()

# 값을 입력 받은 후 비교를 해야 하는데
# 1. [i]부터 시작 해서 해당 값이 m과 같은지, 보다 작은지, 보다 큰지 확인
# 2-1. 같을 경우 cnt +=1 그 후 i 값 증가
# 2-2. 작을 경우 score에 [i] 값 저장 후 i 증가
# 2-2-1. 새로워진 [i] 값과 score를 합한 후 이 값이 m보다 같은지, 보다 작은지, 보다 큰지 확인
# 2-2-2. 같으면 cnt += 1 후 i 증가, 작으면 cnt 저장 후 i 증가, 크면 score = 0 후 i 증가
# 2-3-1. 클 경우 i 증가
# 내가 짠 거는 하나 하나 비교 하기 때문에 시간이 너무 오래걸린다 