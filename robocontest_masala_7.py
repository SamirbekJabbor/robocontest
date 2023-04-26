n = input()
n = int(n)
a=1
b=1
i=0
k=0
while i<n-2:
    c=a+b
    a=b
    b=c
    i=i+1
print(b*2)
