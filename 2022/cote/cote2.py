def solution(rooms, target):
    answer = []
    d = dict()
    cnt_wh = dict()

    for i in rooms:
      tmp = i.replace('[', '').split(']')
      member = tmp[1].split(',')
      for i in member:
        if i in answer:
          cnt_wh[i] = cnt_wh.get(i, 0) + 1
          answer.append(answer.pop(answer.index(i)))
        else:
          answer.append(i)
          cnt_wh[i] = 1
          
      d[tmp[0]] = tmp[1]
    
    for i in answer:
      if i in d[str(target)]:
        answer.remove(i)

    return answer

solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403)