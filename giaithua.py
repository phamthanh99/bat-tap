n=input('nhap n:')
a=int(n)
s=1
for i in range(1,a+1,1):
    s=s*i
    print(s,end='*')
print(' giai thua so',n,'la',s)
