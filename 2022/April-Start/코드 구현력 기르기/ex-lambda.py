def plus_one(x):
    return x +1

lambda_plus = lambda x : x+1
print(lambda_plus(1))

a = [1,2,3]

print(list(map(plus_one, a)))

print(list(map(lambda x : x + 1, a))) # lambda 이런 경우 편하네
