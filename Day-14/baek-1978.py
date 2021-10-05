import math

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

tc = int(input())
n_list = list(map(int, input().split()))
count = 0

for i in n_list:
    if is_prime_number(i):
        count += 1

print(count)
