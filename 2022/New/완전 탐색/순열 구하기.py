chk = []
cnt = 0

def my():
  global chk
  global cnt
  n, m = map(int, input().split())
  chk = [0] * (n + 1)
  li = [0] * m

  dfs(0, n, m, li)
  print(cnt)

# x = 인덱스, na = 숫자 범위, nm = 갯수, lm = 배열
def dfs(x, na, ma, lm):
  global chk
  global cnt

  if x == ma:
    print(' '.join(map(str, lm)))
    cnt += 1
    return
  else:
    for i in range(1, na+1):
      if chk[i] == 1:
        pass
      else:
        chk[i] = 1
        lm[x] = i
        dfs(x+1, na, ma, lm)
        # 여기 돌고나서 돌아오면 0으로 다시 바꿔준다.
        chk[i] = 0
        
my()

# 순열은 본인을 중복해서 뽑지는 못한다.
# 여기서 조금 새로운 관점이 보이네 생각을 못했던 부분이 나오네
# 아 바로 이해 가네