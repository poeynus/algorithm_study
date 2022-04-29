def my():
  mak = list(input())
  stack = []
  sum = 0
  chk = True

  for i in mak:
    if i == '(':
      stack.append(i)
      chk = True
    elif i == ')' and chk:
      chk = False
      stack.pop()
      sum += len(stack)
    elif i == ')' and chk == False:
      stack.pop()
      sum += 1
      chk = False
  print(sum)

def solution():
  s = input()
  stack = []
  cnt = 0
  for i in range(len(s)):
    if s[i] == '(':
      stack.append(s[i])
    else:
      stack.pop()
      if s[i-1] == '(':
        cnt += len(stack)
      else:
        cnt += 1
  print(cnt)

my()

# ( 이거는 무지성 append ) 나오면 이전에 들어간 거 보고 레이저면 pop한 현재 스택 길이 sum에 합치기
# 레이저가 아닌 막대면 스택에서 ( 제거하고 sum += 1 하기
# 휴 풀었다.
