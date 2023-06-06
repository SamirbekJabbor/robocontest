def top(n):
    result = []
    k, j = n-1, 0
    for i in range(1,n+1):
        if i%2 == 1:
            result.append(k)
            k -= 1
        else:
            result.append(j)
            j += 1
    return result
t = int(input())
x = []
for i in range(t):
    n,k = map(int, input().split())
    x.append(top(n).index(k))
for i in x:
    print(i)
