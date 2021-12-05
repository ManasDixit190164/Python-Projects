for _ in range(int(input())):
    c1, c2, c3 = map(str, input().split())
    x, y = map(str, input().split())
    if x == c1 or x == c2 and y != c1:
        print(x)
    else:
        print(y)
