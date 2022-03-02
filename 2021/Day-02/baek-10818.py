num = int(input())
num_list = list(map(int, input().split()))

print(min(num_list), end=" ")
print(max(num_list))