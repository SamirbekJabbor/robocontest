n = int(input())
s = 1
for i in range(n):
    l = list(map(int, input().split()))
    k = [i for i in range(l[0],l[1]+1) if i!=0]
    s *= len(k)
print(s % (10**9 + 7))
