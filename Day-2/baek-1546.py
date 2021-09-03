num = int(input())
report = list(map(int, input().split()))
max_num = max(report)
result = []
score = 0

for i in report:
    result.append(i/max_num*100)

for i in result:
    score += i

print(score/num)
