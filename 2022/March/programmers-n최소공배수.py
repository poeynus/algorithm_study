from math import lcm

def solution(arr):
    flag = True
    count = 1

    while flag:
        tmp = max(arr) * count
        sum = 0

        for i in arr:
            if tmp % i == 0:
                sum += 1
                pass
            else:
                count += 1
                break

        if(sum == len(arr)):
            flag = False
        else:
            pass

    answer = max(arr) * count

    return answer

def secSolution(arr):
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            print(arr[0])
            return arr[0]

secSolution([2,6,8,14])

# [2,6,8,14]	168
# [1,2,3]	6

# 일단 직접 짜고 그 다음에 라이브러리 쓰자
# 입력 값 중 가장 큰 값으로 시작 
# 나머지 값들로 가장 큰 값을 나눠 보고 나머지가 모두 0이면 그 값은 최소 공배수
# 0이 안되면 큰 값을 증가 시키고 또 비교 무한 반복