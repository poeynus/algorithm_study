def my():
  n = int(input())
  in_list = list(map(int, input().split()))
  original = [0] * n

  for i in range(n):
    cnt = 0
    for j in range(n):
      if original[j] == 0:
        cnt += 1
      if cnt == in_list[i] + 1:
        original[j] = i + 1
        break

  print(original)

def solution():
  n = int(input())
  a = list(map(int, input().split()))
  a.insert(0,0)
  seq=[0]*n
  for i in range(1,n+1):
    for j in range(n):
      if a[i]==0 and seq[j]==0:
        seq[j] = i
        break
      elif seq[j]==0:
        a[i]-=1
  for x in seq:
    print(x, end=' ')

def master():
  n = int(input())
  a =list(map(int,input().split()))
  a = a[::-1]
  ans=[]

  for x in a:
    ans.insert(x,n)
    n -=1
  print(ans)

my()

# 너무 어렵게 생각했다.
# 앞에 비어있는 칸의 개수를 생각하면 된다. 1부터 차례대로 앞에 비어있는 칸의 개수를 세고 넣으면 된다.
# 만약 숫자가 있으면 그것은 비어있지 않은 것으로 본다.

# 이거는 그냥 풀었다. 독특한 천재의 방법 또한 가져왔다