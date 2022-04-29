def solution(sizes):
  big_list = []
  small_list = []

  for i in sizes:
    if i[0] < i[1]: 
      i[0], i[1] = i[1], i[0]
    big_list.append(i[0])
    small_list.append(i[1])

  return max(big_list) * max(small_list)


solution([[60, 50], [30, 70], [60, 30], [80, 40]])

# 큰 값을 왼쪽으로 몰고 작은 값을 오른쪽으로 몰고 max 해서 구하면 되지 않을까?