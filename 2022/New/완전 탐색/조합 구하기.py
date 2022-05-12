cnt = 0

def my():
  n, m = map(int, input().split())
  p = [0] * m  # 범위 1 ~ m

  # d = depth, s = 시작 값
  def dfs(d, s):
    global cnt
    if d == m:
      print(' '.join(map(str, p)))  
      cnt += 1
    else:
      for i in range(s, n + 1):
        p[d] = i
        dfs(d+1, i+1) 

  dfs(0, 1)
  print(cnt)

my()

# 함수 안에 하나 더 만들어서 푸니까 훨씬 좋네 매개변수 5개씩 넣던떄보다 수월하다.