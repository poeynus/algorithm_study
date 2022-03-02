import itertools

n, m = map(int, input().split())
card = list(map(int, input().split()))
ans = 0

for i in itertools.combinations(card, 3):
    temp = sum(i)
    
    if ans < temp <= m:
        ans = temp

print(ans)