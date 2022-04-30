def my():
  n = list(input())
  stack = []

  for i in range(len(n)):
    if n[i].isdigit():
      stack.append(int(n[i]))
    else:
      a = stack.pop()
      b = stack.pop()
      if n[i] == '+':
        stack.append(b + a)
      elif n[i] == '-':
        stack.append(b - a)
      elif n[i] == '*':
        stack.append(b * a)
      elif n[i] == '/':
        stack.append(b / a)
  print(stack[0])

def solution():
  # 풀이 방식이 같음
  pass

my()

# 이거는 쉽게 풀었다.