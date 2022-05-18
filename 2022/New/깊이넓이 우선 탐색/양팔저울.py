def my():
  n = int(input())
  chu = list(map(int, input().split()))
  result = set()

  def dfs(d, s):
    if d == n:
      if s not in result and s > 0:
        result.add(s)
    else:
      dfs(d + 1, s + chu[d])
      dfs(d + 1, s - chu[d])
      dfs(d + 1, s)

  dfs(0, 0)

  print(sum(chu) - len(result))

my()

# 아 이건 문제 이해 하는게 어려웠네
# dfs로 다 구하고 중복 제거하는 방식으로
# 가지치기 할 거 없나? 중간에 음수일때 짜르면 뒤에 큰 값 들어올 때는 문제 생기고 흠

# 일단 list와 set의 시간 복잡도 차이가 상당히 크다 O(n) => O(1)
# 중복 되지 않는 값을 저장할 때는 그냥 set 써서 시간 땡기자