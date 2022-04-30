def my():
    n = int(input())

    for i in range(n):
        word = input().lower()

        if word == word[::-1]:
            print(f"#{i+1} YES")
        else:
            print(f"#{i+1} NO")

def solution():
    n=int(input())

    for i in range(n):
        s=input()
        s=s.upper()
        size = len(s)

        for j in range(size//2):
            if s[j]!=s[-1-j]:
                print("#%d NO" %(i+1))
        else:
            print("#%d YES" %(i+1))

my()

# 첫 줄에 n 입력 차례대로 문자열 입력
# 앞에서 읽거나 뒤집어서 읽어도 같으면 YES 아니면 NO
# 그냥 입력 받고 뒤집어서 같은가 확인하면 되네
# 강사님은 하나 하나 다 하셨네