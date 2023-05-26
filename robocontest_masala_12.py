n = int(input())
k = 0
for i in range(2,n+1):
    x = True
    for j in range(2,int(i**0.5) + 1):
        if i%j ==0:
            x = False
            break
    if x:
        k += 1
if k%2 == 0:
    print("Bobur")
else:
    print("Ali")
