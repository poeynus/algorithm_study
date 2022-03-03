import random


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
## 이거도 틀린 것은 아닌데 길다.
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = {}

for i in range(len(price)):
    _dict.append((fruit[i], price[i])) # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}

## zip을 활용하면 더 간결하게 구성할 수 있다.
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]

_dict = dict(zip(fruit, price)) # {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}

## dict안에 데이터가 있는지 없는지 in으로 직접 테스트하지 말고 setdefault를 써서 간편하게 하자
print(_dict.setdefault('strawberry', 0)) # 0