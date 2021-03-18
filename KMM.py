b=int(input("number 1 :"))
c=int(input("number 2 :"))
if b<c:
    max=c
else:
    max=b
for m in range(max , (b*c)+1):
    if m%b==0 and m%c==0:
        kmm=m
        break
print("K.M.M", kmm)
