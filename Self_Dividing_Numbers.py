a=int(input())
b=int(input())
for num in range(a,b+1):
  f=True
  digits=str(num)
  for digit in digits:
    if int(digit)%10==0 or num%int(digit)!=0:
        f=False
  if f==True:
      print(num,end=" ")