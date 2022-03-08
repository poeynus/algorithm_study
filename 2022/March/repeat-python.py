import random
from collections import defaultdict, Counter
import itertools

_list = [1,2,3,4,5]

# 가변인자
first, second, *rest, last = _list
print(rest)

# unpacking
print(*_list)

# packing - tuple
d = first, second, *rest, last
print(d)

# list comprehension
# 앞쪽에 붙는 if는 삼항 연산자의 if라고 생각하시면 되고, 
# 맨 끝에 붙는 if는 값을 넣을지, 뺄지 결정하는 조건이라고 생각하시면 됩니다.
square = [[x ** 2 for x in range(3)] for _ in range(3)]
s_list = [2 * i for i in range(10)]
tmp = [random.randrange(1, 200) for i in range(100)]
t_list = [i for i in tmp if i % 3 == 0]
f_list = [i if i <= 15 else 15 for i in tmp]

# list에서 in 함수와 set에서 in 함수의 차이는 엄청나다. list = O(n), set = O(1)

# dictonary
## zip을 활용하면 더 간결하게 구성할 수 있다.
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]

_dict = dict(zip(fruit, price)) # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}

print(*_dict.keys())
print(*_dict.values())
print(*_dict.items())
## dict안에 데이터가 있는지 없는지 in으로 직접 테스트하지 말고 setdefault를 써서 간편하게 하자
## dict안에 해당하는 값이 없으면 두 번째 인자 값을 리턴
print(_dict.setdefault('strawberry', 0)) # 0

## 이건 좀 신기해서 적어 놓음
## 동일한 key를 가진 값 들을 배열로 묶어줌
movie_review = [('Train to Busan', 4), ('Clementine', 5), ('Parasite', 4.5), ('Train to Busan', 4.2), ('Train to Busan', 4.5), ('Clementine', 5)]

index = defaultdict(list)

for review in movie_review:
    index[review[0]].append(review[1])

print(index) # {'Train to Busan': [4, 4.2, 4.5], 'Clementine': [5, 5], 'Parasite': [4.5]}

## 역순 정렬
so_list = [5,6,3,4,2,1]
soso_list = sorted(so_list, reverse=True)


## 람다 사용 정렬
_slist = [(1, 3), (8, 2), (2, 5), (4, 7)]
sorted_list = sorted(_slist, key = lambda dt: dt[1]) # (8, 2), (1, 3), (2, 5), (4, 7)

## 문자 람다 사용 정렬
_flist = ["CHicken", "hamburger", "Sushi", "chocolate"]

print(sorted(_flist)) # ['CHicken', 'Sushi', 'chocolate', 'hamburger']
print(sorted(_flist, key = lambda dt: dt.lower())) # ['CHicken', 'chocolate', 'hamburger', 'Sushi']

## 문자열 뒤집기
gg = 'I am Hungry...'
print(gg[::-1])
print("".join(reversed(gg)))

## 자주 쓰이는 치트기 itertools
_list = [1, 2, 3, 4]
iter=itertools.combinations(_list,2) # 12 13 14 23 24 34    중복이 없고 순서를 구분하지 않는 모든 조합
iter=itertools.permutations(_list,2) # 12 13 14 21 23 24 31 32 34 41 42 43      중복은 없지만 순서를 구분하는 순열
iter=itertools.combinations_with_replacement(_list,2) # 11 12 13 14 22 23 24 33 34 44       중복이 가능한 조합
iter=itertools.product(_list,repeat=2) # 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44    모든 가능한 경우의 수


## 더하기가 필요하면 sum 써라
## 리스트 입맛대로 출력 하려면 join 써라
## 두 단어를 바꿔야 하면 swap 해라    a , b = b , a

## enumrate
_list = ["a", "b", "c", "d", "e", "f", "g"]
for idx, val in enumerate(_list):
    print(idx, val) # 목표: (0, a), (1, b), (2, c)...

## Counter를 단어 셀 때만 간단하게 썼었는데 이런 방법도 있다.
Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
Counter('hello world').most_common(2) # [('l', 3), ('o', 2)]