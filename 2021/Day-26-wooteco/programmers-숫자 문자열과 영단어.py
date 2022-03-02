def solution(s):
    answer = 0

    n_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    c_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(10):
        s = s.replace(c_list[i], n_list[i])
    
    answer = int(s)

    return answer


solution("one4seveneight")

# "one4seveneight"	1478
# "23four5six7"	234567
# "2three45sixseven"	234567
# "123"	123