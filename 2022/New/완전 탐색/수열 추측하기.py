import sys

def my():
  n, f = map(int, input().split())
  b = [1] * n # 규칙 저장
  p = [0] * n # 수열 저장
  chk = [0] * (n+1) # 수열에 넣을지 말지 판정

  for i in range(1, n):
    b[i] = b[i-1] * (n - i) // i

  def dfs(d, all):
    if d == n and all == f:
      print(' '.join(map(str, p)))
      sys.exit()
    else:
      for i in range(1, n+1):
        if chk[i] == 0:
          p[d] = i
          chk[i] = 1
          dfs(d+1, all + (b[d] * p[d]))
          chk[i] = 0

  dfs(0, 0)

my()

# 함수 안에 함수를 선언해서 사용하기 VS 별도의 함수로 선언해서 작동하기 어떤 것이 더 나은 방법일까
# 함수 안에 함수는 확실히 입력 받는 매개 변수가 줄어들어서 보기가 쉬워진다. -> 이 문제로 처음 짜봤음
# 별도의 함수로 선언 시에는 매개변수가 너무 많아진다. -> 지금 까지 짜던 방식
# 백준은 별도의 함수로 선언해도 global 변수로 받아서 하면 되는데 programmers는 함수로 답안은 제출 하는 방식이라 global에 무리가 있다.(입력이 함수 안에서 작동)

# 피드백 받은 결과
# 경우에 따라서 다르게