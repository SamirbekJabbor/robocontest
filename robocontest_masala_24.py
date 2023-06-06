h,m,s=list(map(int,input().split()))
h1,m1,s1=list(map(int,input().split()))
h<=23 and m<=59 and s<=59
h1<=23 and m1<=59 and s1<=59
a=(h*3600)+(m*60)+(s*1)
b=(h1*3600)+(m1*60)+(s1*1)
if a==b :
  print(0)
else:
  print(abs(b-a))
