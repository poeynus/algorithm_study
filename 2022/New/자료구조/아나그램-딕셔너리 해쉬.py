def my():
  ana = input()
  bnb = input()

  ad = dict()
  bd = dict()

  ali = list(set(ana))
  bli = list(set(bnb))

  ali.sort()
  bli.sort()

  if ali == bli:
    for i in range(len(ali)):
      ad[ali[i]] = ana.count(ali[i])
      bd[bli[i]] = bnb.count(bli[i])
    if ad == bd:
      print('YES')
    else:
      print('NO')
  else:
    print('NO')


def solution():
  a=input()
  b=input()
  sH=dict()
  for x in a:
      sH[x]=sH.get(x, 0)+1
  for x in b:
      sH[x]=sH.get(x, 0)-1

  for x in a:
      if(sH.get(x)>0):
          print("NO")
          break
  else:
      print("YES")

my()

# 일단 입력 받고 count 써서 해당 문자의 개수를 짝지으면 될 거 같다. a : 1, 
# set 써서 중복을 모두 제거하고 여기서 하나씩 꺼내면서 dict에 저장하자
# 두 개 비교해서 같으면 YES 아니면 NO

# 입력 예제로는 맞는데 다른 케이스 나오면 나는 문제 틀린거네, 그래서 수정함
# 강사님꺼 개선된 코드인데 느낌있네
# 동일한지 개수 구하고 비교하는 것은 앞으로 이렇게 접근해야겠다.
# 2개 비교할 때 앞에거는 +1 뒤에거는 -1 해서 다 0이면 같고 하나라도 아니면 다르고