def my():
  sudo = [list(map(int, input().split())) for _ in range(9)]

  for i in range(9):
    if i+1 not in sudo[i]:
      return print('NO')

  a = b = c = 0

  for j in range(3):
    for k in range(3):
      a += sudo[j][k]
    for k in range(3, 6):
      b += sudo[j][k]
    for k in range(6, 9):
      c += sudo[j][k]

  if a == 45 and b == 45 and c == 45:
    a = b = c = 0
  else: 
    return print("NO")

  for j in range(3, 6):
    for k in range(3):
      a += sudo[j][k]
    for k in range(3, 6):
      b += sudo[j][k]
    for k in range(6, 9):
      c += sudo[j][k]

  if a == 45 and b == 45 and c == 45:
    a = b = c = 0
  else: 
    return print("NO")

  for j in range(6, 9):
    for k in range(3):
      a += sudo[j][k]
    for k in range(3, 6):
      b += sudo[j][k]
    for k in range(6, 9):
      c += sudo[j][k]

  if a == 45 and b == 45 and c == 45:
    a = b = c = 0
  else: 
    return print("NO")
  return print("YES")

def solution():
  a=[list(map(int, input().split())) for _ in range(9)]
  if check(a):
    print("YES")
  else:
    print("NO")

def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

my()

# 이 문제는 다행히도 크기가 9 x 9 로 고정이다
# 이거 진짜 머리 아프네 풀긴 했는데 더 쉽게 할 수 있지 않았을까