def my():
  pre = input()
  stack = []
  result = ''

  for i in range(len(pre)):
    if pre[i].isdigit():
      result += pre[i]
    else:
      if stack:
        if pre[i] == '+' or pre[i] == '-':
          if stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '*' or stack[-1] == '/' or stack[-1] == ')':
            while True:
              if len(stack) == 0:
                break
              if stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '*' or stack[-1] == '/' or stack[-1] == ')':
                result += stack.pop()
              else: 
                stack.append(pre[i])
                break
          else:
            stack.append(pre[i])
        elif pre[i] == '*' or pre[i] == '/':
          if stack[-1] == '*' or stack[-1] == '/':
            result += stack.pop()
            stack.append(pre[i])
          else:
            stack.append(pre[i])
        elif pre[i] == '(':
          stack.append(pre[i])
        elif pre[i] == ')':
          while True:
            if stack[-1] == '(':
              stack.pop()
              break
            result += stack.pop()
      else:
        stack.append(pre[i])
  
  while stack:
    result += stack.pop()
  
  print(result)


def solution():
  a=input()
  stack=[]
  res=''
  for x in a:
      if x.isdecimal():
          res+=x
      else:
          if x=='(':
              stack.append(x)
          elif x=='*' or x=='/':
              while stack and (stack[-1]=='*' or stack[-1]=='/'):
                  res+=stack.pop()
              stack.append(x)
          elif x=='+' or x=='-':
              while stack and stack[-1]!='(':
                  res+=stack.pop()
              stack.append(x)
          elif x==')':
              while stack and stack[-1]!='(':
                  res+=stack.pop()
              stack.pop()
  while stack:
      res+=stack.pop()
  print(res)

my()

# ()
# * /
# + -
# 이거는 숫자랑 연산자랑 별도로 분리 해야 한다.
# 연산자 스택에 새로운 연산자가 들어갈때 스택에 있는 것이 우선 순위가 높거나 같으면 먼저 스택에 있는거 내보낸 후 저장
# 여는 괄호는 무조건 append 하고 닫는 괄호 나오면 출력

# 난장판인데 제대로 짜지도 못했네