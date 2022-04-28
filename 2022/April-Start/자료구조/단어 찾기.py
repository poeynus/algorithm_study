def my():
  n = int(input())
  words = [input() for _ in range(n)]
  tmp = [input() for _ in range(n-1)]
  
  print(''.join(list(set(words) - set(tmp))))
        

def solution():
  n=int(input())
  p=dict()
  for i in range(n):
      word=input()
      p[word]=1
  for i in range(n-1):
      word=input()
      p[word]=0
  for key, val in p.items():
      if val==1:
          print(key)
          break

my()

# 반복문을 2번 써서 받으면 되지 않을까
# 1번은 n까지 2번은 n-1까지
# 2번은 받을때 부터 in으로 비교 있으면 pass 없으면 이거 출력 하고 break