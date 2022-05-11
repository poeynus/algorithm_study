def solution(atmos):
  cnt = 0
  day = 0
  mask = False

  for i in atmos:
    if i[0] >= 151 and i[1] >= 76:
      day = 0
      cnt += 1 
      mask = False
    elif i[0] >= 81 or i[1] >= 36:
      day += 1
      mask = True
    elif i[0] <= 80 and i[1] <= 35 and mask:
      day += 1
    elif i[0] <= 80 and i[1] <= 35 and mask == False:
      pass
    else:
      day += 1
      
    if day == 3 and mask:
      cnt += 1
      day = 0
      mask = False
  
  if day != 0 and mask:
    cnt += 1
  return cnt

solution([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]])

# 24분 걸렸다.