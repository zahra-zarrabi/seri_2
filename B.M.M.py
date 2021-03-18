b=int(input("number 1 :"))
c=int(input("number 2 :"))
if b>c :
    max=b
else:
    max=c
for i in range(2,max+1):
    if((b%i==0) and (c%i==0)):
        bmm=i
print("B.M.M :  ", bmm)