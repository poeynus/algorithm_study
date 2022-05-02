result = 0

def my():
  global result
  c, n = map(int, input().split())
  dog = [int(input()) for _ in range(n)]
  a_dog = sum(dog)
  dfs(0, 0, dog, c, 0, a_dog)
  print(result)

  
# x = 인덱스, to = 다 더하거나 뺀 값, arr = 바둑이 배열, ma = 무게 제한, la = 앞으로 계산 할 값들 전체 합, sarr = 바둑이 전체 합
def dfs(x, to, arr, ma, la, sarr):
  global result
  if to > result:
    return
  if to + sarr - la < result:
    return
  if x >= len(arr): # 여기서 비교 하면 됨
    if to <= ma and to > result:
      result = to
      return 
  else:
    dfs(x+1, to + arr[x], arr, ma, la + arr[x], sarr)  
    dfs(x+1, to, arr, ma, la + arr[x], sarr)

my()

# 부분 집합을 전부 만들어서 가장 입력값의 크기를 넘지 않는 가장 큰 무게 구하기

# 1. cut edge 생각 안하고 그냥 dfs로 다 갈기기
# 범위는 인덱스가 넘지 않을때 까지
# 넣는 것 안 넣는 것 다 구해서 c랑 비교 후 c보다 작고 result보다 크면 result를 변경 그 후 print
# ok 잘 된다 하지만 시간 초과

# 2. cut edge 생각하고 하나씩 쳐내기
# dfs 진행하면서 나온 total과 앞으로 진행할 값 전부를 더해도 result보다 작으면 그때 바로 쳐내기
# 캬 시간 바로 줄어드네 체감 기가막히네

# 3. 더 감소 시키기 위하여
# 더한 값이 c보다 크면 return