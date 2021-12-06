from sys import stdin
import collections

try:
    for i in range(int(stdin.readline())):
        n = int(stdin.readline())
        l = list(map(int,input().strip().split()))
        t = set(l)
        if n == 1 or l.count(l[0]) == n:
            print(0)
        elif(len(t) == n):
            print(-1)
        else:
            f = collections.Counter(l)
            v = list(f.values())
            m = max(v)
            s = sum(v)-m
            print(s+1)
except:
    pass