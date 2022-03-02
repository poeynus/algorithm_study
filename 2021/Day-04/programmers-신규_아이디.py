# 첫 번째 풀이 테스트 케이스 1개 실패
# import re

# def solution(new_id):
#     new_id = list(re.sub(r"[^a-zA-Z0-9\.\-\_]","",new_id.lower()))
    
#     a = []

#     for i in range(len(new_id)):
#         if new_id[i] == "." and new_id[i-1] == new_id[i]:
#             pass
#         else:
#             a.append(new_id[i])
    
#     if(len(a) > 2 and a[0] == "."):
#        del a[0]
#     if(len(a) > 2 and a[-1] == "."):
#         del a[-1]

#     new_id = a[0:15]

#     if(len(new_id) > 2 and new_id[0] == "."):
#        del new_id[0]
#     if(len(new_id) > 2 and new_id[-1] == "."):
#         del new_id[-1]

#     if new_id == []:
#         new_id.append("a")

#     if len(new_id) < 3:
#         while len(new_id) < 3:
#             new_id.append(new_id[-1])

#     answer = ""
#     return answer


# 두 번째 풀이
import re

def solution(new_id):
    new_id = re.sub("[^a-z0-9\.\-\_]","",new_id.lower())
    new_id = re.sub("\.+", ".", new_id)
    new_id = re.sub("^\.|\.$", '', new_id)
    if new_id == "":
        new_id = "a"
    new_id = re.sub("\.$", '', new_id[0:15])
    while len(new_id) < 3:
        new_id += new_id[-1]
    answer = new_id

    return answer
