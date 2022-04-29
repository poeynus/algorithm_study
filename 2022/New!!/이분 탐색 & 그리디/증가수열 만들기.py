def my():
  n = int(input())
  in_list = list(map(int,input().split()))
  v = 0
  result = ''
  cnt = 0

  while True:
    if in_list[0] < in_list[-1] and in_list[0] > v:
      result += 'L'
      cnt += 1
      v = in_list.pop(0)
    elif in_list[0] > in_list[-1] and in_list[-1] > v:
      result += 'R'
      cnt += 1
      v = in_list.pop()
    elif in_list[0] < in_list[-1] and in_list[-1] > v:
      result += 'R'
      cnt += 1
      v = in_list.pop()
    elif in_list[0] > in_list[-1] and in_list[0] > v:
      result += 'L'
      cnt += 1
      v = in_list.pop(0)
    else:
      break
  print(cnt)
  print(result)

def solution():
  n = int(input())
  a = list(map(int,input().split()))
  lt = 0
  rt = n - 1
  last=0
  res=""
  tmp=[]
  while lt<=rt:
    if a[lt]>last:
      tmp.append((a[lt], 'L'))
    if a[rt]>last:
      tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) ==0:
      break
    else:
      res = res+tmp[0][1]
      last=tmp[0][0]
      if tmp[0][1] == 'L':
        lt+=1
      else:
        rt-=1
    tmp.clear()
    
  print(res)
my()

# 일단 0 선언하고, 리스트에서 왼쪽 오른쪽 값 중 가장 0보다는 크고 작은 값 가져와서 출력 이 값은 저장
# 만약 큰 값이 없으면 종료
# 왼쪽에서 빼면 L, 오른쪽에서 빼면 R