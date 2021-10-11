tc = int(input())

for i in range(tc):
    score = list(map(int, input().split()))
    count = 0
    ave = sum(score[1:])/score[0]

    for i in range(1, score[0]+1):
        if score[i] >  ave:
            count += 1

    print("{:.3f}%".format(count / score[0] * 100))