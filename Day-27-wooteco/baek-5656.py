cnt = 0

while True:
    a, calc, b = map(str, input().split())
    cnt += 1

    a = int(a)
    b = int(b)

    if calc == "E":
        break
    elif calc == ">":
        print(f"Case {cnt}: {str(a > b).lower()}")
    elif calc == "<":
        print(f"Case {cnt}: {str(a < b).lower()}")    
    elif calc == ">=":
        print(f"Case {cnt}: {str(a >= b).lower()}")
    elif calc == "<=":
        print(f"Case {cnt}: {str(a <= b).lower()}")
    elif calc == "==":
        print(f"Case {cnt}: {str(a == b).lower()}")
    elif calc == "!=":
        print(f"Case {cnt}: {str(a != b).lower()}")