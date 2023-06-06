import math
t = int(input())
res = []
for i in range(t):
    a, b, c = map(int, input().split())
    a, b = min(a,b), max(a,b)
    if c < b and c%math.gcd(a,b) == 0:
        res.append("YES")
    else:
        res.append("NO")
for i in res:
    print(i)
