n = int(input())
for i in range(1,n+1):
    t = True
    k = i%100
    if k + i != n:
        t = False
    if t:
        print(i,end=' ')
