a1,a2,a3 = list(map(int,input().split()))
a4,a5,a6 = list(map(int,input().split()))
a7,a8,a9 = list(map(int,input().split()))

b1=abs(a1-6)+abs(a2-1)+abs(a3-8)+abs(a4-7)+abs(a5-5)+abs(a6-3)+abs(a7-2)+abs(a8-9)+abs(a9-4)
b2=abs(a1-6)+abs(a2-7)+abs(a3-2)+abs(a4-1)+abs(a5-5)+abs(a6-9)+abs(a7-8)+abs(a8-3)+abs(a9-4)
b3=abs(a1-2)+abs(a2-9)+abs(a3-4)+abs(a4-7)+abs(a5-5)+abs(a6-3)+abs(a7-6)+abs(a8-1)+abs(a9-8)
b4=abs(a1-2)+abs(a2-7)+abs(a3-6)+abs(a4-9)+abs(a5-5)+abs(a6-1)+abs(a7-4)+abs(a8-3)+abs(a9-8)
b5=abs(a1-4)+abs(a2-3)+abs(a3-8)+abs(a4-9)+abs(a5-5)+abs(a6-1)+abs(a7-2)+abs(a8-7)+abs(a9-6)
b6=abs(a1-4)+abs(a2-9)+abs(a3-2)+abs(a4-3)+abs(a5-5)+abs(a6-7)+abs(a7-8)+abs(a8-1)+abs(a9-6)
b7=abs(a1-8)+abs(a2-1)+abs(a3-6)+abs(a4-3)+abs(a5-5)+abs(a6-7)+abs(a7-4)+abs(a8-9)+abs(a9-2)
b8=abs(a1-8)+abs(a2-3)+abs(a3-4)+abs(a4-1)+abs(a5-5)+abs(a6-9)+abs(a7-6)+abs(a8-7)+abs(a9-2)

if(b2>=b1):
    max=b1
else:
    max=b2

if(b3<=max):
    max=b3

if(b4<=max):
    max=b4

if(b5<=max):
    max=b5

if(b6<=max):
    max=b6

if(b7<=max):
    max=b7

if(b8<=max):
    max=b8

print(max)
