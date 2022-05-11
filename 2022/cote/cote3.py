def solution(line):
    answer = []
    board = [['1','2','3','4','5','6','7','8','9','0'], ["Q","W","E","R","T","Y","U","I","O","P"]]
    le_bo = ['1','2','3','4','5',"Q","W","E","R","T"]
    
    le_hand = [1,0]
    ri_hand = [1,9]
    
    for i in line:
      wid = hei = 0
      rig = lef = 0
      if i in board[0]:
        wid = board[0].index(i)
        rig = abs(wid - ri_hand[1]) + abs(hei - ri_hand[0])
        lef = abs(wid - le_hand[1]) + abs(hei - le_hand[0])
        if rig > lef:
          answer.append(0)
          le_hand = [0, board[0].index(i)]
        elif rig < lef:
          answer.append(1)
          ri_hand = [0, board[0].index(i)]
        elif rig == lef:
          if abs(wid - ri_hand[1]) > abs(wid - le_hand[1]):
            answer.append(0)
            le_hand = [0, board[0].index(i)]
          elif abs(wid - ri_hand[1]) < abs(wid - le_hand[1]):
            answer.append(1)
            ri_hand = [0, board[0].index(i)]
          elif abs(wid - ri_hand[1]) == abs(wid - le_hand[1]):
            if i in le_bo:
              answer.append(0)
              le_hand = [0, board[0].index(i)]
            else:
              answer.append(1)
              ri_hand = [0, board[0].index(i)]
      if i in board[1]:
        wid = board[1].index(i)
        hei = 1
        rig = abs(wid - ri_hand[1]) + abs(hei - ri_hand[0])
        lef = abs(wid - le_hand[1]) + abs(hei - le_hand[0])
        if rig > lef:
          answer.append(0)
          le_hand = [1, board[1].index(i)]
        elif rig < lef:
          answer.append(1)
          ri_hand = [1, board[1].index(i)]
        elif rig == lef:
          if abs(wid - ri_hand[1]) > abs(wid - le_hand[1]):
            answer.append(0)
            le_hand = [1, board[1].index(i)]
          elif abs(wid - ri_hand[1]) < abs(wid - le_hand[1]):
            answer.append(1)
            ri_hand = [1, board[1].index(i)]
          elif abs(wid - ri_hand[1]) == abs(wid - le_hand[1]):
            if i in le_bo:
              answer.append(0)
              le_hand = [1, board[1].index(i)]
            else:
              answer.append(1)
              ri_hand = [1, board[1].index(i)]
    return answer

solution("RYI76")