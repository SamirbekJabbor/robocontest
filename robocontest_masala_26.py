mod = 1000000007
t = int(input())
x = []
for i in range(t):
    n = int(input())
    x.append(n)
for i in x:
    print(i*i % mod)
