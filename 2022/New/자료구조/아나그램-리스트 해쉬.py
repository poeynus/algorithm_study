def my():
  ana = list(input())
  bnb = list(input())

  ana.sort()
  bnb.sort()

  if ana == bnb:
    print('YES')
  else:
    print('NO')

def sec():
  ana = input()
  bnb = input()
  chk = [0] * 52

  for i in range(len(ana)):
    if ana[i].isupper():
      chk[ord(ana[i]) - 65] += 1
      chk[ord(bnb[i]) - 65] -= 1
    else:
      chk[ord(ana[i]) - 71] += 1
      chk[ord(bnb[i]) - 71] -= 1

  if sum(chk) == 0:
    print('YES')
  else:
    print('NO')

def solution():
  a=input()
  b=input()
  str1=[0]*52
  str2=[0]*52
  for x in a:
      if x.isupper():
          str1[ord(x)-65]+=1
      else:
          str1[ord(x)-71]+=1
  for x in b:
      if x.isupper():
          str2[ord(x)-65]+=1
      else:
          str2[ord(x)-71]+=1
  for i in range(52):
      if str1[i]!=str2[i]:
          print("NO")
          break
  else:
      print("YES")

my()

# 이번엔 딕셔너리 말고 list만 써서 해결하기
# 근데 그냥 리스트로 받아서 sort 하고 같으면 같다고 하지 않을까? 이것도 쉽게 되는데 시간이 너무 오래 걸리겠지?

# 2번째 방법 미리 선언 해놓고 a는 해당 위치 1씩 추가 bsms 1씩 빼기 합쳐서 0 나오면 동일하다는 뜻
# 아스키 코드로 만들고 대문자는 - 65, 소문자는 - 65 - 6
# A 65 a 97

# 강사님이 이전에 개선된 방식으로 접근해서 증감 시켜서 풀었다. 더 효율 적인듯