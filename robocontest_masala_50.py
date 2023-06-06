n = int(input())
x = []
for i in range(n):
    x.append(list(map(int, input().split())))
r = ''
for i in x:
    if (i[0]*(i[0] + 1)//2) == i[1]:
        r += '1'
    else:
        r += '0'
print(r)
