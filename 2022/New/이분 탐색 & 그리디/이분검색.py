def my():
  n, m = map(int, input().split())
  in_list = list(map(int, input().split()))
  in_list.sort()
  lt = 0
  rt = len(in_list) - 1
  mid = 0
  
  while lt != rt:
    mid = (lt + rt) // 2
    print(mid, lt, rt)
    if in_list[mid] > m:
      rt = mid - 1
    elif in_list[mid] < m:
      lt = mid + 1
    else:
      print(mid+1)

  

def solution():
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  a.sort()

  lt = 0
  rt = n-1

  while lt <= rt:
    mid = (lt + rt) // 2
    print(mid, lt, rt)
    if a[mid] == m:
      print(mid + 1)
      break
    elif a[mid] > m:
      rt = mid - 1
    elif a[mid] < m:
      lt = mid + 1

solution()

# 입력 받고 기존 리스트에 append 후 find 함수 쓰면 될듯
# 바이너리 서치
# 결과가 나올때 까지 중간 값을 반복적으로 찾아서 도달
# 아이고 잘못 풀었네 내가 짠 코드는 반복문을 덜 돈다.

# 이것만 기억하자 lt, rt, mid를 사용하여서 풀고
# while문의 범위는 lt가 rt보다 크거나 같아질때 까지

# 여기서 부터는 알고리즘을 활용해서 풀이 해야 하네