def my():
  n ,m = map(int, input().split())
  hang = [[0] * n for _ in range(n)]

  for _ in range(m):
    h, y, v = map(int, input().split())
    hang[h-1][y-1] = v

  print(hang)
  
my()