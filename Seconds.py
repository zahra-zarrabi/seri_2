print('Please enter time in seconds:')
a=int(input("second : "))
h=int(a/3600)
a=a%3600
m=int(a/60)
s=a%60
print(h,":",m,":",s)