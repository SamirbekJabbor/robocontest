n = int(input())
x = []
for i in range(n):
    a = input()
    a = bin((int(a)))
    x.append(a.count('1'))
for i in x:
    print(i)
