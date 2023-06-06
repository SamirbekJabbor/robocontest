l = list(map(int, input().split()))
s = 0
for i in range(len(l)):
    s += l[i]//2 + l[i]%2
print(s)
