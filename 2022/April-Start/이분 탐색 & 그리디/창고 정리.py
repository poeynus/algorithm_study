def my():
  n = int(input())
  block = list(map(int, input().split()))
  m = int(input())

  for _ in range(m):
    block[block.index(max(block))] -= 1
    block[block.index(min(block))] += 1

  print(max(block) - min(block))


def solution():
  L=int(input())
  a=list(map(int, input().split()))
  m=int(input())
  a.sort()
  for _ in range(m):
    a[0]+=1
    a[L-1]-=1
    a.sort()

my()

# 예전에 풀어봤던 문제
# 배열로 저장한 후 m회 동안 가장 큰 값 1 감소 가장 작은 값 1 증가
# 마지막 출력때 가장 큰 값 - 가장 작은 값

# 강사님은 정렬 후 맨 앞과 뒤 값을 1씩 증감후 또 정렬하는 방식 뭐가 더 빠르지
# 테스트 해보니까 약간 오락가락이네
# 깨달았다 그리디는 일단 정렬하고 생각하는 것이다.