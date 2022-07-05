mini = 2147000000

def solution(h,k,boxes):
  boxes.append(h)
  if k in boxes:
    start = boxes.index(k)
    boxes.sort()
  else:
    boxes.append(k)
    boxes.sort()
    start = boxes.index(k) - 1
    boxes.remove(k)

  # d = depth, c = count
  def dfs(d, c, ar):
    global mini
    if d == len(boxes) - 1:
      if c < mini:
        mini = c
    else:
      if boxes[d+1] - boxes[d] > k:
        return
      elif boxes[d+1] - boxes[d-1] > k:
        print(boxes[d])
        ar.append(boxes[d])
        dfs(d+1, c+1, ar)
      else:
        dfs(d+1, c, ar)

  dfs(start, 0, [])
  return(mini)

solution(12, 3, [2,3,6,7,8,10,11])