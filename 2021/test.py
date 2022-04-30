def solution(files):
    answer = []
    print('hi')
    return answer


solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])

# 입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

# 입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# 출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

# 입력 받고 3단계로 나눠 HEAD, NUMBER, TAIL
# HEAD는 입력 받고 소문자로 변환 후 숫자가 나오기 전까지로 끊기
# NUMBER는 숫자인지 아닌지만
# TAIL은 나머지 