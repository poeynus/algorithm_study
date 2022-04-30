from collections import deque

def my():
  must = list(input())
  n = int(input())

  for j in range(n):
    d = deque(must)
    words = input()
    
    for i in words:
      if i in d:
        if d[0] == i:
          d.popleft()
        else:
          break
      else:
        pass
    
    print(f'#{j+1} NO') if d else print(f'#{j+1} YES')

def solution():
  need=input()
  n=int(input())
  for i in range(n):
      plan=input()
      dq=deque(need)
      for x in plan:
          if x in dq:
              if x!=dq.popleft():
                  print("#%d NO" %(i+1))
                  break
      else:
          if len(dq)==0:
              print("#%d YES" %(i+1))
          else:
              print("#%d NO" %(i+1))

my()

# 처음에 문자가 deque에 있는지 확인 없으면 그냥 pop
# 있으면 deque 첫 값과 비교해서 일치하면 서로 pop 
# 있는데 deque 첫 값과 다르면 break False
# deque 길이가 0 이 될 때 까지 반복

# 잘 풀었네