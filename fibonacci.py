n=int(input())
s1=0
s2=1
count=0
for i in range(0,n):
    fib=s1
    print(fib,end=' ')
    s1=s2
    s2=fib+s2