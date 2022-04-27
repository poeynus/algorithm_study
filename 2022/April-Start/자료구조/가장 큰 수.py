def my():
  n ,m = map(int, input().split())
  stack = list(map(int, str(n)))
  result = []


  for i in range(len(stack)):
    print(result)
    while m != -1:
      if i == len(stack):
        break
      if len(result) == 0:
        result.append(stack[i])
        break
      if result[-1] > stack[i]:
        result.append(stack[i])
        break
      elif result[-1] < stack[i]:
        result.pop()
        m -= 1

  print(result)


def solution():
  num ,m = map(int, input().split())
  num = list(map(int, str(num)))
  stack =[]

  for x in num:
    while stack and m > 0 and stack[-1] < x:
      stack.pop()
      m-=1
    stack.append(x)

  if m != 0:
    stack = stack[:-m]

  print(''.join(map(str, stack)))

my()

# 숫자리스트와 제거횟수 제공
# 숫자들을 넣는데 자기 앞에 자기보다 작은 수가 있으면 횟수를 1차감 하고 그 숫자를 제거
# 횟수가 끝나면 그대로 삽입
# 다 넣었는데 횟수가 남으면 뒤의 자리 부터 제거

# 나 너무 어렵게 생각했나 못짰네
# 관점을 다르게 생각하자 나는 while문 안에서 추가와 삭제가 모두 일어나게 짰고 강사님은 while문은 삭제만 일어나게 짜서 간단해졌다.