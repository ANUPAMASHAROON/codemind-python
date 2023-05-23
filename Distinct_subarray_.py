l=int(input())
r=int(input())
c=0
for i in range(l,r+1):
    h=0
    for j in range(i,r+1):
        h+=j
        if h%2==1:
            c+=1
print(c)