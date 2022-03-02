def solution(s):

    lowerList = list(map(str, s.split(' ')))
    upperList = []

    print(lowerList)

    for i in lowerList:
        if(i[0:1].isdigit()):
            tmp = i.lower()
            upperList.append(tmp)
        else:
            tmp = i.lower().title()
            upperList.append(tmp)

    answer = ' '.join(upperList)
    return answer


def secSolution(s):

    lowerList = list(map(str, s.split(' ')))
    upperList = []

    for i in lowerList:
        tmp = i.capitalize()
        upperList.append(tmp)
    answer = ' '.join(upperList)
    return answer

solution(" adgagd 3eagdag ")

# "3people unFollowed me"	"3people Unfollowed Me"
# "for the last week"	"For The Last Week"