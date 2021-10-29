def solution(numbers, hand):

    phone = { 1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2), "*":(3, 0), 0:(3, 1), "#":(3,2) }
   
    l_hand = phone["*"]
    r_hand = phone["#"]
    result = []

    for i in numbers:
        if i == 1:
            result.append("L")
            l_hand = phone[1]
        elif i == 4:
            result.append("L")
            l_hand = phone[4]
        elif i == 7:
            result.append("L")
            l_hand = phone[7]
        elif i == 3:
            result.append("R")
            r_hand = phone[3]
        elif i == 6:
            result.append("R")
            r_hand = phone[6]
        elif i == 9:
            result.append("R")
            r_hand = phone[7]
        else:
            n = phone[i]
            l_dist = abs(n[0] - l_hand[0]) + abs(n[1] - l_hand[1])
            r_dist = abs(n[0] - r_hand[0]) + abs(n[1] - r_hand[1])
            
            if(l_dist > r_dist):
                result.append("R")
                r_hand = n
            elif(l_dist < r_dist):
                result.append("L")
                l_hand = n
            else:
                if hand == "right":
                    result.append("R")
                    r_hand = phone[i]
                else:
                    result.append("L")
                    l_hand = phone[i]
    answer = ''.join(result)
    return answer

solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left")

# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"

# dict로 접근 해보기 2차원 배열은 너무 어렵네