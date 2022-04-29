def my():
  n = int(input())
  n_list = list(map(int, input().split()))
  m = int(input())
  m_list = list(map(int, input().split()))

  result = n_list + m_list
  result.sort()
  print(result)

def solution():
  n = int(input())
  n_list = list(map(int, input().split()))
  m = int(input())
  m_list = list(map(int, input().split()))
  p1=p2=0
  c = []
  while p1<n and p2<m:
    if n_list[p1]<=m_list[p2]:
      c.append(n_list[p1])
      p1+=1
    else:
      c.append(m_list[p2])
      p2+=1
  if p1<n:
    c=c+n_list[p1:]
  if p2<m:
    c=c+m_list[p2:]
  print(c)

my()

# 그냥 입력 받고 합친 뒤 sort하면 되겠네
# 강사님 풀이는 입력 값이 무조건 정렬이 되어서 들어온다는 가정하에 사용가능