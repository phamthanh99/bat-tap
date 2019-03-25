n=input('nhap n:')
a=int(n)
for j in range(2,a+1):
    s=0
    for i in range(1,j+1):
        if (j%i==0):
            s=s+1
    if s==2:
        print (j,end=',')
