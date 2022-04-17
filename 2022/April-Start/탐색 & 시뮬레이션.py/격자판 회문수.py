def my():
  in_list = [list(map(int, input().split())) for _ in range(7)]
  cnt = 0

  for i in range(7):
    for j in range(3):
      if in_list[i][j] == in_list[i][j+4] and in_list[i][j+1] == in_list[i][j+3]:
        cnt += 1
    for j in range(3):
      if in_list[j][i] == in_list[j+4][i] and in_list[j+1][i] == in_list[j+3][i]:
        cnt += 1
  print(cnt)

def solution():
  n_list = [list(map(int, input().split())) for _ in range(7)]
  cnt = 0
  for i in range(3):
      for j in range(7):
          tmp = n_list[j][i : i + 5]
          if tmp == tmp[::-1]:
              cnt += 1
          for k in range(2):
              if n_list[i + k][j] != n_list[i + 5 - k - 1][j]:
                  break
          else:
              cnt += 1
  print(cnt)

my()

# 이것도 다행인게 크기가 정해진 7*7 배열
# 이거는 그냥 조건 걸어서 풀어버렸음 크기가 고정이기에 가능한 방법
# 몰랐는데 이차원 배열도 그냥 슬라이스 되네