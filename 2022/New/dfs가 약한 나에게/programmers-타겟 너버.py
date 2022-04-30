answer = 0

def solution(numbers, target):
    global answer
    chk = [0] * len(numbers)
    dfs(0, chk, numbers, target)
    print(answer)
    return answer

def dfs(x, arr, num, tar):
  res = 0
  global answer
  if x == len(arr):
    for i in range(len(arr)):
      if arr[i] == 1:
        res += num[i]
      else:
        res -= num[i]
    if res == tar:
      answer += 1
  else:
    arr[x] = 1
    dfs(x + 1, arr, num, tar)
    arr[x] = 0
    dfs(x + 1, arr, num, tar)

solution([4,1,2,1], 2)